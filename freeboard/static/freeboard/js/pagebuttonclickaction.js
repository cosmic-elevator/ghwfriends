

function pageButtonClickAction(page_num) {
    // 리디렉션 
    const url = "http://127.0.0.1:8000/freeboard/?page=" + page_num;
    location.href = url;
}


