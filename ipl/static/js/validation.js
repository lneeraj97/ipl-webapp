

function inRange(playerId) {
    return (parseInt(playerId) > 0 && parseInt(playerId) < 524);
}

function onlyUnique(value, index, self) {
    return self.indexOf(value) === index;
}

function checkLength() {
    var input = document.getElementById("pickedPlayers");
    var inputValues = input.value
    //If Empty
    if (inputValues == "") {
        window.alert("Please enter 11 comma separated Player IDs");
        input.focus();
        return false;
    }
    //If not Empty
    else {
        var list = inputValues.split(",");
        list = list.filter(onlyUnique);
        if (list.length < 11) {
            window.alert("Please enter 11 unique comma separated Player IDs");
            input.focus();
            return false;
        } else if (list.length > 11) {
            window.alert("Please enter only 11 unique Player IDs");
            input.focus();
            return false;
        }
        if (!list.every(inRange)) {
            window.alert("Please enter values between 0 and 524");
            return false;
        }
    }
    return true;

}

function checkCount() {
    var totalBat = document.getElementById("id_batsmen");
    var totalBowl = document.getElementById("id_bowlers");
    var totalAll = document.getElementById("id_allrounders");
    var forBat = document.getElementById("id_foreignBatsmen");
    var forBowl = document.getElementById("id_foreignBowlers");
    var forAll = document.getElementById("id_foreignAllrounders");
    totalCount = parseInt(totalAll.value) + parseInt(totalBat.value) + parseInt(totalBowl.value);
    forCount = parseInt(forBat.value) + parseInt(forBowl.value) + parseInt(forAll.value);
    if (totalCount == 11 && forCount == 4) {
        return true;
    } else {
        window.alert("Total Team : 11 Players\nForeign Players: 4 (Max)");
        return false;
    }
}
