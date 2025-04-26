// Event listener for form submission
document.getElementById('energyForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevents the form from submitting
  
    // Get the input values
    const wattage = parseFloat(document.getElementById('wattage').value);
    const hoursPerDay = parseFloat(document.getElementById('hours').value);
    const rate = parseFloat(document.getElementById('rate').value);
  
    // Validate inputs
    if (isNaN(wattage) || isNaN(hoursPerDay) || isNaN(rate) || wattage <= 0 || hoursPerDay <= 0 || rate <= 0) {
      alert('Please enter valid values for all fields.');
      return;
    }
  
    // Calculate energy consumption (kWh)
    const dailyEnergy = (wattage * hoursPerDay) / 1000; // kWh per day
    const monthlyEnergy = dailyEnergy * 30; // kWh per month (assuming 30 days)
    const yearlyEnergy = dailyEnergy * 365; // kWh per year (assuming 365 days)
  
    // Calculate the cost
    const dailyCost = dailyEnergy * rate;
    const monthlyCost = monthlyEnergy * rate;
    const yearlyCost = yearlyEnergy * rate;
  
    // Display the results
    document.getElementById('dailyCost').textContent = `Daily Cost: ₹${dailyCost.toFixed(2)}`;
    document.getElementById('monthlyCost').textContent = `Monthly Cost: ₹${monthlyCost.toFixed(2)}`;
    document.getElementById('yearlyCost').textContent = `Yearly Cost: ₹${yearlyCost.toFixed(2)}`;
  });
  