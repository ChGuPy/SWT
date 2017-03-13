/**
 * Created by Admin on 06.03.2017.
 */

 function myfunc(qset) {
    var right_answers = 0;
    var qset = qset; //document.getElementsByClassName('jumbotron');

    var buttons = document.getElementsByTagName('button');
    for (var i = 0, len = buttons.length; i < len; i++) buttons[i].addEventListener('click', sendAnswer);

    function sendAnswer(event) {
        answer = event.target.value;
        parent = event.target.parentNode.parentNode.parentNode;
        parent = parent.getAttribute('id');
        $.get('/send_answer/', {a: answer}, function (mes) {
            if (mes == 'Right') {
                right_answers += 1;
            }
            ;
            document.getElementById(parent).style.display = 'none';
            if (document.getElementById('' + (parseInt(parent) + 1))) {
                document.getElementById('' + (parseInt(parent) + 1)).style.display = 'block';
            } else {
                ending();
                if (right_answers <= 1) {
                    document.getElementById('bad_finish').style.display = 'block';
                    document.getElementById('bad_finish_stats').innerHTML = 'Right answers:' + right_answers + '!';
                } else if (right_answers == qset) {
                    document.getElementById('master_finish_stats').innerHTML = 'Right answers: ' + right_answers + '!';
                    document.getElementById('master_finish').style.display = 'block';
                } else {
                    document.getElementById('regular_finish_stats').innerHTML = 'Right answers:' + right_answers + '!';
                    document.getElementById('regular_finish').style.display = 'block';
                }
            }
        });
    }}


