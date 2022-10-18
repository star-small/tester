const addQuestions = document.querySelector(".addQuestions");
const answerBlog = document.querySelector(".answerBlog");

let value = 1;
addQuestions.addEventListener('click',function (e){ 
    const target = e.target;
    if (target && target.classList.contains('addQuestions')){

        for (let i =0; i < value; i ++){
            let i = document.createElement('div');
            console.log('awda');
            i.innerHTML = `                    
            <div class="answerline">
                <input class="text" type="text" name="answers" placeholder="ответ"><input class="radio" type="checkbox" name="right_position" value="${value}" id="radioButton">
            </div>
            `;
            answerBlog.append(i);
        }
    }

});
