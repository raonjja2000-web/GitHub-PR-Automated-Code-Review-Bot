# GitHub-PR-Automated-Code-Review-Bot
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>미성년자 판별</title>
    </head>
    <body>
        <h1>미성년자 판별</h1>
        <input id="input_age" type="number" value="17"/>
        <button id="btn_ok">확인</button>
        <div id="result">성인일까요 미성년자일까요?</div>
    </body>
    <script>
        //1.버튼이 클릭될 시 이벤트 실행
        document.getElementById("btn_ok").onclick=function(){
            //1-1. #input_age의 value 조회
            let age =document.getElementById("input_age").value;
            alert(age);
            //1-2. 해당 나이가 성인인지 미성년자인지 판별
            let result=null;
            if(age>=20){
                result="성인";
            }else{
                result="미성년자";
            }
            //1-3. 판별 결과를 #result에 반영
            document.getElementById("result").textContent=result+"입니다.";
        };
    </script>
</html>
