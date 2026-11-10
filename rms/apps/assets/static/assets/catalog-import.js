(() => {
  const form = document.getElementById("import-form");
  const fileInput = document.getElementById("csv-file");
  const dropZone = document.getElementById("drop-zone");
  const selectedFile = document.getElementById("selected-file");
  const previewButton = document.getElementById("preview-button");
  const formError = document.getElementById("form-error");
  const resultState = document.getElementById("result-state");
  const resultReport = document.getElementById("result-report");
  const resultSubtitle = document.getElementById("result-subtitle");
  const maxBytes = Number(form.dataset.maxBytes) || 10 * 1024 * 1024;
  const maxSizeLabel = `${(maxBytes / 1024 / 1024).toFixed(1)} MiB`;
  const outcomeLabels = {
    would_create: "Would Create (Dự kiến tạo)",
    would_link_reference: "Would Link Reference (Dự kiến liên kết)",
    unchanged: "Unchanged (Không thay đổi)",
    error: "Error (Lỗi)",
    conflict: "Conflict (Xung đột)",
  };

  // Chuyển kích thước byte thành cách ghi ngắn để người dùng biết giới hạn tệp.
  function formatFileSize(bytes) {
    return bytes < 1024 * 1024
      ? `${(bytes / 1024).toFixed(0)} KiB`
      : `${(bytes / 1024 / 1024).toFixed(1)} MiB`;
  }

  // Mã hóa nội dung từ báo cáo trước khi chèn vào bảng HTML.
  function escapeHtml(value) {
    return String(value ?? "").replace(/[&<>"']/g, (character) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[character]);
  }

  function showFormError(message) {
    formError.textContent = message;
    formError.hidden = false;
  }

  function updateSelectedFile() {
    const file = fileInput.files?.[0];
    if (!file) {
      selectedFile.hidden = true;
      selectedFile.textContent = "";
      return;
    }
    selectedFile.innerHTML = `<span class="file-check" aria-hidden="true">✓</span><strong>${escapeHtml(file.name)}</strong><span>${formatFileSize(file.size)}</span>`;
    selectedFile.hidden = false;
    formError.hidden = true;
  }

  function showLoading(message) {
    resultReport.hidden = true;
    resultState.className = "result-empty loading";
    resultState.innerHTML = `<span class="spinner" aria-hidden="true"></span><h3>${escapeHtml(message)}</h3><p>Job sẽ tự chuyển sang kết quả khi xử lý xong.</p>`;
  }

  function showApiError(response, payload) {
    const statusCode = response?.status;
    if (statusCode === 401 || statusCode === 403) {
      return "Phiên đăng nhập không hợp lệ hoặc tài khoản chưa có quyền nhập Catalog (Danh mục). Hãy đăng nhập bằng tài khoản có quyền phù hợp.";
    }
    if (payload?.error?.code === "upload_too_large") {
      return `Tệp vượt quá giới hạn ${maxSizeLabel}. Hãy chọn tệp nhỏ hơn.`;
    }
    if (statusCode === 400) {
      return "Thông tin yêu cầu chưa hợp lệ. Kiểm tra loại dữ liệu, chế độ xem trước và tệp CSV.";
    }
    return "Không gửi được tệp xem trước. Hãy thử lại sau ít phút.";
  }

  function renderReport(run) {
    const rows = run.row_results || [];
    const statusLabel = run.status === "PREVIEWED"
      ? "Previewed (Đã xem trước)"
      : run.status === "FAILED"
        ? "Failed (Thất bại)"
        : run.status;
    const rowsHtml = rows.length
      ? rows.map((row) => {
        const outcome = row.outcome || "error";
        const naturalKey = row.natural_key
          ? `${row.natural_key.catalog_type_code || ""} / ${row.natural_key.code || ""}`
          : "";
        const errorCode = row.error_code ? `<code class="row-key">Error Code (Mã lỗi): ${escapeHtml(row.error_code)}</code>` : "";
        return `<tr>
          <td>${escapeHtml(row.row_number)}</td>
          <td><span class="outcome ${escapeHtml(outcome)}">${escapeHtml(outcomeLabels[outcome] || "Error (Lỗi)")}</span></td>
          <td><div class="row-message">${escapeHtml(row.message || "Không có mô tả lỗi.")}</div>${naturalKey ? `<code class="row-key">${escapeHtml(naturalKey)}</code>` : ""}${errorCode}</td>
        </tr>`;
      }).join("")
      : `<tr><td colspan="3">Tệp không có dòng dữ liệu để xem trước.</td></tr>`;

    resultState.hidden = true;
    resultReport.hidden = false;
    resultSubtitle.textContent = `Job #${run.id} · ${statusLabel}`;
    resultReport.innerHTML = `<div class="summary-grid">
      <div class="summary-card"><strong>${escapeHtml(run.total_rows)}</strong><span>Total Rows (Tổng số dòng)</span></div>
      <div class="summary-card success"><strong>${escapeHtml(run.would_create_count)}</strong><span>Would Create (Dự kiến tạo)</span></div>
      <div class="summary-card"><strong>${escapeHtml(run.would_link_reference_count)}</strong><span>Would Link Reference (Dự kiến liên kết)</span></div>
      <div class="summary-card"><strong>${escapeHtml(run.unchanged_count)}</strong><span>Unchanged (Không đổi)</span></div>
      <div class="summary-card error"><strong>${escapeHtml(run.error_count)}</strong><span>Errors (Dòng lỗi)</span></div>
    </div>
    <div class="run-status"><span>${escapeHtml(statusLabel)} · Import Run (Lần nhập) #${escapeHtml(run.id)}</span><a href="${escapeHtml(run.status_url)}" target="_blank" rel="noopener">Mở API Report (Báo cáo API) ↗</a></div>
    <div class="table-wrap"><table class="result-table"><thead><tr><th>CSV Row (Dòng CSV)</th><th>Outcome (Kết quả)</th><th>Details (Chi tiết)</th></tr></thead><tbody>${rowsHtml}</tbody></table></div>
    <div class="report-footer"><button id="new-preview" class="secondary-button" type="button">Preview Another File (Xem trước tệp khác)</button><span class="safe-note"><span>✓</span> Chưa ghi Catalog Item (Mục danh mục).</span></div>`;
    document.getElementById("new-preview").addEventListener("click", resetReport);
  }

  function resetReport() {
    resultReport.hidden = true;
    resultState.hidden = false;
    resultState.className = "result-empty";
    resultState.innerHTML = `<div class="empty-illustration" aria-hidden="true"><span>▤</span><i></i><i></i><i></i></div><h3>Chưa có báo cáo</h3><p>Tải CSV lên và chọn Preview Import (Xem trước nhập liệu) để kiểm tra từng dòng.</p>`;
    resultSubtitle.textContent = "Báo cáo kiểm tra sẽ hiển thị tại đây.";
  }

  async function getRun(statusUrl) {
    const response = await fetch(statusUrl, {
      credentials: "same-origin",
      headers: { Accept: "application/json" },
    });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(showApiError(response, payload));
    return payload;
  }

  // Theo dõi job cho đến khi preview hoàn tất hoặc worker báo lỗi.
  async function pollRun(statusUrl, attempts = 0) {
    try {
      const run = await getRun(statusUrl);
      if (["PREVIEWED", "FAILED", "REJECTED", "COMPLETED"].includes(run.status)) {
        renderReport(run);
        previewButton.disabled = false;
        return;
      }
      if (attempts >= 60) {
        showLoading("Job vẫn đang xử lý");
        resultState.innerHTML += `<p><a href="${escapeHtml(statusUrl)}" target="_blank" rel="noopener">Kiểm tra Import Run (Lần nhập) trực tiếp ↗</a></p>`;
        previewButton.disabled = false;
        return;
      }
      showLoading(run.status === "QUEUED" ? "Job đang chờ worker" : "Đang kiểm tra CSV");
      window.setTimeout(() => pollRun(statusUrl, attempts + 1), 1500);
    } catch (error) {
      resultState.className = "result-empty";
      resultState.innerHTML = `<h3>Chưa tải được báo cáo</h3><p>${escapeHtml(error.message)}</p><button id="retry-report" class="secondary-button" type="button">Tải lại báo cáo</button>`;
      document.getElementById("retry-report").addEventListener("click", () => pollRun(statusUrl));
      previewButton.disabled = false;
    }
  }

  fileInput.addEventListener("change", updateSelectedFile);
  for (const eventName of ["dragenter", "dragover"]) {
    dropZone.addEventListener(eventName, (event) => {
      event.preventDefault();
      dropZone.classList.add("dragging");
    });
  }
  for (const eventName of ["dragleave", "drop"]) {
    dropZone.addEventListener(eventName, (event) => {
      event.preventDefault();
      dropZone.classList.remove("dragging");
    });
  }
  dropZone.addEventListener("drop", (event) => {
    const file = event.dataTransfer.files?.[0];
    if (file) {
      fileInput.files = event.dataTransfer.files;
      updateSelectedFile();
    }
  });

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    formError.hidden = true;
    const file = fileInput.files?.[0];
    if (!file) {
      showFormError("Chọn CSV File (Tệp CSV) trước khi xem trước.");
      return;
    }
    if (!file.name.toLowerCase().endsWith(".csv")) {
      showFormError("Chỉ nhận tệp có phần mở rộng .csv.");
      return;
    }
    if (file.size > maxBytes) {
      showFormError(`Tệp vượt quá giới hạn ${maxSizeLabel}.`);
      return;
    }

    previewButton.disabled = true;
    previewButton.innerHTML = `<span class="spinner" aria-hidden="true"></span> Đang gửi tệp…`;
    showLoading("Đang tạo Import Run (Lần nhập)");
    try {
      const formData = new FormData(form);
      const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;
      const response = await fetch("/api/v2/assets/imports/", {
        method: "POST",
        credentials: "same-origin",
        headers: { Accept: "application/json", "X-CSRFToken": csrfToken },
        body: formData,
      });
      const payload = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(showApiError(response, payload));
      resultSubtitle.textContent = `Job #${payload.id} · Queued (Đang chờ)`;
      await pollRun(payload.status_url);
    } catch (error) {
      resultState.className = "result-empty";
      resultState.innerHTML = `<h3>Không tạo được job</h3><p>${escapeHtml(error.message || "Đã có lỗi. Hãy thử lại.")}</p>`;
      previewButton.disabled = false;
    } finally {
      previewButton.innerHTML = `<span aria-hidden="true">⌕</span> Preview Import (Xem trước nhập liệu)`;
    }
  });
})();
