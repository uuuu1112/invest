function createStockTable(stockData) {
    console.log("print stock data",stockData)
    // 创建一个表格元素
    var table = document.createElement('table');
    table.border = '1';

    // 创建表头行
    var headerRow = table.insertRow(0);
    for (var key in stockData[0]) {
        var headerCell = document.createElement('th');
        headerCell.innerHTML = key;
        headerRow.appendChild(headerCell);
    }

    // 添加数据行
    for (var i = 0; i < stockData.length; i++) {
        var dataRow = table.insertRow(i + 1);
        for (var key in stockData[i]) {
            var dataCell = dataRow.insertCell();
            dataCell.innerHTML = stockData[i][key];
        }
    }

    // 将表格添加到页面中的容器
    var tableContainer = document.getElementById('table-container');
    tableContainer.appendChild(table);
}

// 你的股票数据
// var stockData=JSON.parse('{{ api_data | tojson | escapejs | safe }}');
var stockData = [
    {
        "代號": "8080",
        "名稱": "永利聯合",
        "成交": 10.4,
        "ROE(%)": 179.0,
        "EPS(元)": 7.76,
        "盈餘配發率": 0.0,
        "最小EPS": 0.12,
        "內部成長率": 179.0,
        "目標價": 1389.04,
        "預期報酬率": "13256.15%"
    },
    {
        "代號": "5864",
        "名稱": "致和證",
        "成交": 21.4,
        "ROE(%)": 28.7,
        "EPS(元)": 5.12,
        "盈餘配發率": -47.6,
        "最小EPS": 0.19,
        "內部成長率": 42.3612,
        "目標價": 216.889344,
        "預期報酬率": "913.50%"
    }
];

// 调用函数将股票数据转换为表格
createStockTable(stockData);