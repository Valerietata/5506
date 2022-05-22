
var tileSelected = null;
var numSelected = null;
var wrongsteps = 0;
// var board = [
//     "--74916-5",
//     "2---6-3-9",
//     "-----7-1-",
//     "-586----4",
//     "--3----9-",
//     "--62--187",
//     "9-4-7---2",
//     "67-83----",
//     "81--45---"
// ]
var board = [
    "38749-625",
    "24-568379",
    "569327418",
    "758619234",
    "123784596",
    "496253187",
    "934176852",
    "675832941",
    "812945763"
]
var solution = [
    "387491625",
    "241568379",
    "569327418",
    "758619234",
    "123784596",
    "496253187",
    "934176852",
    "675832941",
    "812945763"
]
//to create a board
//class completedtile is for setting bg color of given tile number
for (i = 0; i < 9; i++) {
    for (j = 0; j < 9; j++) {
        if (board[i][j] != '-') {
            var element = '<div class="tile completedtile" id= ' + i.toString() + j.toString() + '>' + board[i][j] + '</div>';
            $('#board').append(element);
        }
        else {
            var element = '<div class="tile" id= ' + i.toString() + j.toString() + '></div>';
            $('#board').append(element);
        }
        //add gridlines to divide the board into 9 sections
        if (i === 2 | i === 5) {
            $('#' + i.toString() + j.toString()).addClass('horizontallines');

        }
        if (j === 2 | j === 5) {
            $('#' + i.toString() + j.toString()).addClass('verticallines');
        }
    }

}
//create an eventListener for selected number

$('.digit').click(function () {
    if (numSelected != null) {
        $(numSelected).removeClass('selectedDight');
    }
    $(this).addClass('selectedDight');
    numSelected = this;

})
//create an eventListener for tile event
$('.tile').click(function () {
    //give a number to a tile only if it's empty
    if ($(this).text() != "") {
        return;
    }
    //record the coordinate of clicked tiles once selecting a number 
    if (numSelected != null) {
        $(this).text($(numSelected).text());
        var tilecoord = $(this).attr("id");
    }
    //compare the coordinate of a clicked tile with its corresponding solution coord.
    var m = tilecoord[0];
    var n = tilecoord[1];
    if ($(this).text() === solution[m][n]) {
        $(this).addClass('correctanswer');
        setTimeout(() => {
            $(this).removeClass('correctanswer');
        }, 200);

    }
    else {
        $(this).addClass('wronganswer');
        wrongsteps += 1;
        $('#errors').text(wrongsteps);
        setTimeout(() => {
            $(this).text("");
            $(this).removeClass('wronganswer');
        }, 300);
    }

})
//submit file
$(".submitbutton").click(function () {
    for (a = 0; a < 9; a++) {
        for (b = 0; b < 9; b++) {
            if ($("#" + a + b).text() === "") {
                alert(' Unfinished Game!');
                return;

            }
        }
    }
    //pass wrongsteps to back end
    var data = wrongsteps;
    $.ajax(
            {
                url:"http://127.0.0.1:5000/user/ranking",
                type:"post",
                data : {
                    "wrong_moves" : data
                },
                success: function(d){
                    alert("Congratulations!");
                    window.location.replace("http://127.0.0.1:5000/user/allranking");
                },
                error : function (d){
                    alert("Opps, connection failed....");
                }
            })

})


//responding button color change after clicking
$(".submitbutton,.newgamebutton").click(function () {
    $(this).addClass('changebuttoncolor');
    setTimeout(() => {
        $(this).removeClass('changebuttoncolor');
    }, 100);

})
//reload page
$(".newgamebutton").click(function () {
    location.reload();
})
