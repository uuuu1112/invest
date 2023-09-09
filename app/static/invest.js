function disableSubmitButton() {
    // 禁用提交按鈕
    var submitButton = document.getElementById("submit-button");
    submitButton.disabled = true;
}

// 開啟對話框
function openDialog() {
    document.getElementById('overlay').style.display = 'block';
}

// 關閉對話框
function closeDialog() {
    document.getElementById('overlay').style.display = 'none';
}

// 送出對話框（在此處添加您的送出邏輯）
function submitDialog() {
    alert('對話框已送出');
    closeDialog();
}

// 點擊背景關閉對話框
window.onclick = function(event) {
    var overlay = document.getElementById('overlay');
    if (event.target == overlay) {
        closeDialog();
    }
}
