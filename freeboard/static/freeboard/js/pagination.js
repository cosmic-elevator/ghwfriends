

// 템플릿 내부의 JavaScript 부분

    // 클릭 시 색 바꾸기
var current_page = 1;
document.getElementById(current_page).style.backgroundColor = 'yellow';
var elements = document.getElementsByClassName("page-button");
for (var i = 0, length = elements.length; i < length; i++) {
    elements[i].style.backgroundColor = 'gray';
}


function pageButtonClickAction(id) {
    // 클릭 시 색 바꾸기
    var elements = document.getElementsByClassName("page-button");
    for (var i = 0, length = elements.length; i < length; i++) {
        elements[i].style.backgroundColor = 'gray';
    }
    document.getElementById(id).style.backgroundColor = 'yellow';


    // Ajax를 사용하여 서버에 요청을 보냅니다.
    $.ajax({
        type: 'GET',
        url: '/list/',  // 해당 URL을 적절히 수정
        data: {'page': pageNumber},
        success: function(response) {
            // 서버에서 받은 응답으로 게시물을 업데이트합니다.
            updatePageWithNewData(response.objects);
        },
        error: function(error) {
            console.log(error);
        }
    });


}

    

function updatePageWithNewData(objects) {
    // 서버에서 받은 객체를 사용하여 HTML을 업데이트합니다.
    // 예: 동적으로 생성된 HTML을 추가하거나 기존 HTML을 교체합니다.
    var contentContainer = document.getElementById('content-container');
    contentContainer.innerHTML = '';  // 현재 내용을 지우고 새로운 내용으로 채움

    for (var i = 0; i < objects.length; i++) {
        var objectHTML = '<h5><a href="' + objects[i].url + '">' + objects[i].title + '</a></h5>';
        contentContainer.innerHTML += objectHTML;
    }
}
