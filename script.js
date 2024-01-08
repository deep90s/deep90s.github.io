function validateNumberInput(value, errorMessage) {
    if (isNaN(value) || value <= 0) {
        document.getElementById("result").innerHTML = errorMessage;
        return false;
    }
    return true;
}

function calculateRisk() {
    var riskPercentage = parseFloat(document.getElementById("riskPercentage").value);
    if (!validateNumberInput(riskPercentage, "Invalid risk percentage input. Please enter a valid positive number.")) {
        return;
    }

    var entryPrice = parseFloat(document.getElementById("entryPrice").value);
    if (!validateNumberInput(entryPrice, "Invalid entry price input. Please enter a valid positive number.")) {
        return;
    }

    var stopLossPrice = entryPrice - (entryPrice * riskPercentage / 100);
    document.getElementById("calculatedRisk").value = stopLossPrice.toFixed(2);

    var totalRiskDollars = document.getElementById("totalRiskDollars");
    if (totalRiskDollars.value.trim() === "") {
        var totalCapital = parseFloat(document.getElementById("totalCapital").value);
        var calculatedDollars = (riskPercentage / 100) * totalCapital;
        totalRiskDollars.value = calculatedDollars.toFixed(2);
    }

    var totalRiskPercentage = document.getElementById("totalRiskPercentage");
    if (totalRiskPercentage.value.trim() === "") {
        totalRiskPercentage.value = riskPercentage.toFixed(2);
    }

    document.getElementById("result").innerHTML = "";
}

function updatePositionSize() {
    var totalCapital = parseFloat(document.getElementById("totalCapital").value);
    var totalRiskPercentage = parseFloat(document.getElementById("totalRiskPercentage").value);
    var totalRiskDollars = parseFloat(document.getElementById("totalRiskDollars").value);

    if (isNaN(totalRiskPercentage) && isNaN(totalRiskDollars)) {
        document.getElementById("result").innerHTML = "Invalid total risk input. Please enter either percentage or dollars.";
        return;
    }

    var totalRisk;
    if (!isNaN(totalRiskPercentage)) {
        totalRisk = (totalRiskPercentage / 100) * totalCapital;
    } else {
        totalRisk = totalRiskDollars;
    }

    var entryPrice = parseFloat(document.getElementById("entryPrice").value);
    var stopLossPrice = parseFloat(document.getElementById("calculatedRisk").value);

    if (entryPrice - stopLossPrice === 0) {
        document.getElementById("result").innerHTML = "Invalid position size calculation. Entry price and stop loss price are the same.";
        return;
    }

    var positionSize = Math.ceil(totalRisk / (entryPrice - stopLossPrice));
    document.getElementById("positionSize").value = positionSize;

    // New code to calculate Capital Per Stock and Amount Per Trade
    var numberOfStocks = parseFloat(document.getElementById("numberOfStocks").value);
    var capitalPerStock = totalCapital / numberOfStocks;
    document.getElementById("capitalPerStock").value = capitalPerStock.toFixed(2);

    var amountPerTrade = entryPrice * positionSize;
    document.getElementById("amountPerTrade").value = amountPerTrade.toFixed(2);
}

document.getElementById("totalRiskPercentage").addEventListener("input", updatePositionSize);
document.getElementById("totalRiskPercentage").addEventListener("change", updatePositionSize);

document.getElementById("totalRiskDollars").addEventListener("input", updatePositionSize);
document.getElementById("totalRiskDollars").addEventListener("change", updatePositionSize);

document.getElementById("calculatedRisk").addEventListener("input", updatePositionSize);
document.getElementById("calculatedRisk").addEventListener("change", updatePositionSize);

function calculateRiskAndPositionSize() {
    calculateRisk();
    updatePositionSize();
}

function resetFields() {
    document.getElementById("totalCapital").value = "";
    document.getElementById("numberOfStocks").value = "";
    document.getElementById("totalRiskPercentage").value = "";
    document.getElementById("totalRiskDollars").value = "";
    document.getElementById("entryPrice").value = "";
    document.getElementById("riskPercentage").value = "";
    document.getElementById("calculatedRisk").value = "";
    document.getElementById("positionSize").value = "";
    document.getElementById("capitalPerStock").value = "";
    document.getElementById("amountPerTrade").value = "";
    document.getElementById("result").innerHTML = "";
}
