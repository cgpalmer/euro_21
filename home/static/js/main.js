$(document).ready(function () {

const names_of_players = ["Joe", "Maddie", "Chris", "Shannon", "Tori", "Jack", "Luke", "Dan"]


    for (i = 0; i < names_of_players.length; i++) {
        console.log(`${names_of_players[i]}_score`);
        let score_value = $(`#${names_of_players[i]}_score`).val();
      
        console.log(score_value)
        $(`.${names_of_players[i]}`).width(`${score_value}%`);
        console.log(names_of_players[i]);
    }

});