$(document).ready(function () {

const names_of_players = ["Joe", "Maddie", "Chris", "Shannon", "Tori", "Jack", "Luke", "Dan"]


    for (i = 0; i < names_of_players.length; i++) {
        console.log(`${names_of_players[i]}_score`);
        let score_value = $(`#${names_of_players[i]}_score`).val();
      
        console.log(score_value)
        $(`.${names_of_players[i]}`).width(`${score_value}%`);
        console.log(names_of_players[i]);
    }

    for (i = 0; i < names_of_players.length; i++) {
        console.log(`${names_of_players[i]}_ga`);
        let score_value = $(`#${names_of_players[i]}_ga`).val();
      
        console.log(score_value)
        $(`.${names_of_players[i]}_ga`).width(`${score_value}%`);
        console.log(names_of_players[i]);
    }

    for (i = 0; i < names_of_players.length; i++) {
        console.log(`${names_of_players[i]}_gf`);
        let score_value = $(`#${names_of_players[i]}_gf`).val();
      
        console.log(score_value)
        $(`.${names_of_players[i]}_gf`).width(`${score_value}%`);
        console.log(names_of_players[i]);
    }

     for (i = 0; i < names_of_players.length; i++) {
        console.log(`${names_of_players[i]}_og`);
        let score_value = $(`#${names_of_players[i]}_og`).val();
      
        console.log(score_value)
        $(`.${names_of_players[i]}_og`).width(`${score_value}%`);
        console.log(names_of_players[i]);
    }

});