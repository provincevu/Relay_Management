(() => {
  const stationList = document.getElementById("station-list");
  const stationSearch = document.getElementById("station-search");
  const stationCount = document.getElementById("station-count");
  const stationPageLabel = document.getElementById("station-page-label");
  const stationPrev = document.getElementById("station-prev");
  const stationNext = document.getElementById("station-next");
  const stationDetail = document.getElementById("station-detail");
  const treeContent = document.getElementById("tree-content");
  const state = { stations: [], selectedStation: null, depth: "relays", treeQuery: "" };
  let stationSearchTimer;
  let treeSearchTimer;

  // Chuyển chuỗi từ API thành nội dung an toàn trước khi chèn vào giao diện.
  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, (character) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[character]);
  }

  // Gọi API bằng phiên đăng nhập hiện tại và chuẩn hóa lỗi thành thông báo để hiển thị.
  async function fetchJson(url) {
    const response = await fetch(url, { credentials: "same-origin", headers: { Accept: "application/json" } });
    const body = await response.json().catch(() => ({}));
    if (!response.ok) {
      // Giữ thông báo tiếng Việt; không đưa nguyên văn lỗi kỹ thuật của máy chủ lên màn hình.
      const error = new Error("Không thể tải dữ liệu.");
      error.status = response.status;
      throw error;
    }
    return body;
  }

  // Hiển thị lỗi theo ngữ cảnh và gắn thao tác thử lại vào đúng khu vực bị lỗi.
  function showError(container, error, retry) {
    const message = error.status === 403
      ? "Tài khoản chưa được cấp quyền xem Assets (Tài sản) trong phạm vi này."
      : error.status === 401
        ? "Phiên đăng nhập đã hết hạn. Hãy đăng nhập lại để tiếp tục."
        : error.status === 404
          ? "Không tìm thấy dữ liệu được yêu cầu."
          : error.status >= 500
            ? "Máy chủ đang gặp sự cố. Hãy thử lại sau ít phút."
            : "Đã có lỗi khi tải dữ liệu. Hãy thử lại.";
    container.innerHTML = `<div class="error-state"><span class="error-symbol">!</span><p>${escapeHtml(message)}</p><button type="button" class="retry-button">Thử tải lại</button></div>`;
    container.querySelector("button")?.addEventListener("click", retry, { once: true });
  }

  // Vẽ danh sách trạm, cập nhật phân trang và chọn trạm đầu tiên nếu kết quả thay đổi.
  function renderStations(payload) {
    state.stations = payload.results || [];
    stationCount.textContent = `${payload.count || 0} Stations (Trạm) trong phạm vi của bạn`;
    stationPageLabel.textContent = state.stations.length ? `Hiển thị ${state.stations.length} Stations (Trạm)` : "Không có kết quả";
    stationPrev.disabled = !payload.previous;
    stationNext.disabled = !payload.next;
    stationPrev.onclick = payload.previous ? () => loadStations(payload.previous) : null;
    stationNext.onclick = payload.next ? () => loadStations(payload.next) : null;

    if (!state.stations.length) {
      state.selectedStation = null;
      stationList.innerHTML = `<div class="empty-state"><span class="empty-state-icon">⌕</span><h3>Không tìm thấy Stations (Trạm)</h3><p>Thử từ khóa khác hoặc xóa nội dung tìm kiếm.</p></div>`;
      stationDetail.className = "detail-header empty-detail";
      stationDetail.innerHTML = `<div class="empty-icon" aria-hidden="true">⌖</div><div><h2>Không có Station (Trạm) phù hợp</h2><p>Thử thay đổi từ khóa tìm kiếm.</p></div>`;
      treeContent.innerHTML = "";
      return;
    }

    stationList.innerHTML = state.stations.map((station) => {
      const selected = state.selectedStation?.id === station.id;
      const location = station.location || station.organization?.name || "Chưa có địa điểm";
      return `<button class="station-item${selected ? " selected" : ""}" type="button" data-station-id="${escapeHtml(station.id)}">
        <span class="station-avatar" aria-hidden="true">⌖</span>
        <span class="station-meta"><strong>${escapeHtml(station.name)}</strong><span>${escapeHtml(station.code)} · ${escapeHtml(location)}</span></span>
        <span class="station-arrow" aria-hidden="true">›</span>
      </button>`;
    }).join("");

    stationList.querySelectorAll("[data-station-id]").forEach((button) => {
      button.addEventListener("click", () => {
        const station = state.stations.find((item) => String(item.id) === button.dataset.stationId);
        if (station) selectStation(station);
      });
    });

    const selectedStillVisible = state.stations.some((item) => item.id === state.selectedStation?.id);
    if (!state.selectedStation || !selectedStillVisible) selectStation(state.stations[0]);
  }

  // Tải trang trạm theo từ khóa và báo lỗi trong danh sách nếu API từ chối truy cập.
  async function loadStations(url = null) {
    stationList.innerHTML = `<div class="loading-row"><span class="spinner"></span>Đang tải trạm…</div>`;
    const targetUrl = url || buildStationUrl();
    try {
      const payload = await fetchJson(targetUrl);
      renderStations(payload);
    } catch (error) {
      stationCount.textContent = "Chưa tải được danh sách";
      showError(stationList, error, () => loadStations(targetUrl));
    }
  }

  // Tạo URL chỉ từ các tham số API đang hỗ trợ.
  function buildStationUrl() {
    const params = new URLSearchParams();
    const query = stationSearch.value.trim();
    if (query) params.set("q", query);
    params.set("page", "1");
    return `/api/v2/assets/stations/?${params.toString()}`;
  }

  // Cập nhật trạm đang chọn và tải cây tài sản từ API theo station ID.
  function selectStation(station) {
    state.selectedStation = station;
    renderStations({ results: state.stations, count: Number(stationCount.textContent.match(/^\d+/)?.[0] || state.stations.length) });
    const voltage = station.voltage_level?.name ? ` · ${station.voltage_level.name}` : "";
    stationDetail.className = "detail-header";
    stationDetail.innerHTML = `<div class="empty-icon" aria-hidden="true">⌖</div>
      <div><h2>${escapeHtml(station.name)}</h2><span class="station-code">Station (Trạm): ${escapeHtml(station.code)}</span></div>
      <div class="detail-pills"><span class="detail-pill"><strong>Organization (Đơn vị)</strong> ${escapeHtml(station.organization?.name || "Chưa xác định")}</span><span class="detail-pill"><strong>Location (Địa điểm)</strong> ${escapeHtml(station.location || "Chưa cập nhật")}${escapeHtml(voltage ? ` · Voltage Level (Cấp điện áp)${voltage}` : "")}</span></div>`;
    loadTree();
  }

  // Vẽ các ngăn lộ và các rơ-le đang hoạt động nếu người dùng chọn mức chi tiết.
  function renderTree(payload, keepSearchFocus = false) {
    const bays = payload.results || [];
    const relayCount = bays.reduce((sum, bay) => sum + (bay.relays?.length || 0), 0);
    const countLabel = `${payload.count || 0} Bays (Ngăn lộ)${state.depth === "relays" ? ` · ${relayCount} Relays (Rơ-le) trên trang` : ""}`;
    // Mỗi Bay là một thẻ; Relay nằm bên trong Bay để thể hiện đúng quan hệ tài sản.
    const bayCards = bays.map((bay) => {
      const voltage = bay.rated_voltage ? `Voltage (Điện áp): ${escapeHtml(bay.rated_voltage)} kV` : "Chưa có điện áp";
      const current = bay.rated_current ? `Current (Dòng điện): ${escapeHtml(bay.rated_current)} A` : "Chưa có dòng định mức";
      const relays = (bay.relays || []).map((relay) => `<div class="relay-row">
        <span class="relay-mark" aria-hidden="true">⌁</span>
        <span class="relay-info"><strong>${escapeHtml(relay.name)}</strong><span>Relay (Rơ-le): ${escapeHtml(relay.code)}${relay.manufacturer?.name ? ` · Manufacturer (Nhà sản xuất): ${escapeHtml(relay.manufacturer.name)}` : ""}</span></span>
        ${relay.model_name ? `<span class="relay-model">Model (Mẫu thiết bị): ${escapeHtml(relay.model_name)}</span>` : ""}
      </div>`).join("");
      return `<article class="bay-card"><div class="bay-heading"><span class="bay-symbol" aria-hidden="true">▤</span>
        <span class="bay-info"><strong>${escapeHtml(bay.name)}</strong><span>Bay (Ngăn lộ): ${escapeHtml(bay.code)}</span></span>
        <span class="bay-metrics"><span>${voltage}</span><span>${current}</span></span></div>
        ${state.depth === "relays" ? `<div class="relay-list">${relays || `<div class="relay-row"><span class="relay-info"><span>Chưa có Relays (Rơ-le) đang hoạt động</span></span></div>`}</div>` : ""}
      </article>`;
    }).join("");

    treeContent.innerHTML = `<div class="tree-toolbar">
      <label class="search-box tree-search" for="bay-search"><span aria-hidden="true">⌕</span><input id="bay-search" type="search" placeholder="Lọc Bays (Ngăn lộ) theo mã hoặc tên" value="${escapeHtml(state.treeQuery)}" autocomplete="off"></label>
      <div class="view-toggle" role="group" aria-label="Mức chi tiết"><button type="button" data-depth="bays" class="${state.depth === "bays" ? "active" : ""}">Bays (Ngăn lộ)</button><button type="button" data-depth="relays" class="${state.depth === "relays" ? "active" : ""}">Bays + Relays (Ngăn lộ + Rơ-le)</button></div>
    </div>
    <div class="tree-content-inner"><div class="tree-summary"><span><strong>${escapeHtml(state.selectedStation?.code || "")}</strong> · Asset Tree (Cây tài sản)</span><span>${escapeHtml(countLabel)}</span></div>
      ${bays.length ? bayCards : `<div class="empty-state"><span class="empty-state-icon">▤</span><h3>Chưa có Bays (Ngăn lộ) phù hợp</h3><p>Thử xóa bộ lọc hoặc kiểm tra dữ liệu của Station (Trạm) này.</p></div>`}
      ${payload.next || payload.previous ? `<div class="tree-pagination"><button class="icon-button" type="button" data-tree-page="previous" aria-label="Trang trước" ${payload.previous ? "" : "disabled"}>‹</button><span>Trang Bays (Ngăn lộ)</span><button class="icon-button" type="button" data-tree-page="next" aria-label="Trang sau" ${payload.next ? "" : "disabled"}>›</button></div>` : ""}
    </div>`;

    treeContent.querySelectorAll("[data-depth]").forEach((button) => button.addEventListener("click", () => {
      state.depth = button.dataset.depth;
      loadTree();
    }));
    const baySearch = document.getElementById("bay-search");
    if (keepSearchFocus) {
      baySearch.focus();
      baySearch.setSelectionRange(baySearch.value.length, baySearch.value.length);
    }
    baySearch.addEventListener("input", () => {
      state.treeQuery = baySearch.value;
      clearTimeout(treeSearchTimer);
      treeSearchTimer = setTimeout(() => loadTree(), 280);
    });
    treeContent.querySelector('[data-tree-page="previous"]')?.addEventListener("click", () => loadTree(payload.previous));
    treeContent.querySelector('[data-tree-page="next"]')?.addEventListener("click", () => loadTree(payload.next));
  }

  // Tải cây trạm, hỗ trợ lọc Bay và phân trang mà không bỏ qua giới hạn quyền của API.
  async function loadTree(url = null) {
    if (!state.selectedStation) return;
    const keepSearchFocus = document.activeElement?.id === "bay-search";
    treeContent.innerHTML = `<div class="loading-row"><span class="spinner"></span>Đang tải cấu trúc tài sản…</div>`;
    const params = new URLSearchParams({ depth: state.depth, page_size: "25" });
    if (state.treeQuery.trim()) params.set("q", state.treeQuery.trim());
    const targetUrl = url || `/api/v2/assets/stations/${encodeURIComponent(state.selectedStation.id)}/tree/?${params.toString()}`;
    try {
      const payload = await fetchJson(targetUrl);
      renderTree(payload, keepSearchFocus);
    } catch (error) {
      showError(treeContent, error, () => loadTree(targetUrl));
    }
  }

  stationSearch.addEventListener("input", () => {
    clearTimeout(stationSearchTimer);
    stationSearchTimer = setTimeout(() => loadStations(), 280);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
      event.preventDefault();
      stationSearch.focus();
    }
  });
  loadStations();
})();
