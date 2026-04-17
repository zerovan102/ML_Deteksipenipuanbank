document.getElementById('fraudForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const radarContainer = document.getElementById('radar');
    const resultDisplay = document.getElementById('resultDisplay');
    const btnScan = document.querySelector('.btn-scan');
    
    // UX: Start Scanning Animation
    radarContainer.classList.remove('hidden');
    resultDisplay.classList.add('hidden');
    radarContainer.classList.add('scanning');
    btnScan.disabled = true;
    btnScan.innerHTML = '<span>Scanning Features...</span>';
    
    // Gather form data
    const transactionData = {
        TransactionAmount: parseFloat(document.getElementById('TransactionAmount').value),
        TransactionType: parseInt(document.getElementById('TransactionType').value),
        Location: parseInt(document.getElementById('Location').value),
        Channel: parseInt(document.getElementById('Channel').value),
        CustomerAge: parseInt(document.getElementById('CustomerAge').value),
        CustomerOccupation: parseInt(document.getElementById('CustomerOccupation').value),
        TransactionDuration: parseInt(document.getElementById('TransactionDuration').value),
        LoginAttempts: parseInt(document.getElementById('LoginAttempts').value),
        AccountBalance: parseFloat(document.getElementById('AccountBalance').value),
        TransactionHour: parseInt(document.getElementById('TransactionHour').value),
        DayOfWeek: parseInt(document.getElementById('DayOfWeek').value),
        TimeSinceLast: parseFloat(document.getElementById('TimeSinceLast').value)
    };

    try {
        // Mocking network delay slightly to ensure the scan animation is visible (aesthetic purpose)
        await new Promise(resolve => setTimeout(resolve, 1500));

        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(transactionData)
        });

        if (!response.ok) {
            throw new Error(`Server returned ${response.status}`);
        }

        const result = await response.json();
        
        // Stop scanning
        radarContainer.classList.remove('scanning');
        radarContainer.classList.add('hidden');
        
        // Populate Result Display
        populateResults(result);

    } catch (error) {
        console.error('Prediction failed:', error);
        alert('An error occurred while analyzing the transaction. Ensure the backend server is running and the ML model is accessible.');
        
        // Reset state on error
        radarContainer.classList.remove('scanning');
        btnScan.disabled = false;
        btnScan.innerHTML = '<span>Analyze Transaction</span><i data-feather="zap"></i>';
        feather.replace();
    }
});

function populateResults(result) {
    const resultDisplay = document.getElementById('resultDisplay');
    const badge = document.getElementById('riskBadge');
    const probText = document.getElementById('probabilityText');
    const sysMsg = document.getElementById('systemMsg');
    const meterFill = document.getElementById('meterFill');

    resultDisplay.classList.remove('hidden');
    
    // Animate percentage text
    animateValue(probText, 0, result.probability, 1000);
    
    // Reset classes
    badge.className = 'risk-badge';
    
    // Set colors and message based on risk level returned from FastAPI
    if (result.prediction === 3) {
        badge.classList.add('risk-critical');
        badge.innerText = 'CRITICAL FRAUD RISK';
        sysMsg.innerText = 'Signature matched known fraud attacks. Override block recommended.';
        meterFill.style.background = '#EF4444';
        meterFill.style.width = '95%';
        meterFill.style.boxShadow = '0 0 20px #EF4444';
    } else if (result.prediction === 2) {
        badge.classList.add('risk-high');
        badge.innerText = 'HIGH RISK ACTIVITY';
        sysMsg.innerText = 'Suspicious velocity and spatial mismatch detected. Manual review advised.';
        meterFill.style.background = '#F59E0B';
        meterFill.style.width = '75%';
        meterFill.style.boxShadow = '0 0 20px #F59E0B';
    } else if (result.prediction === 1) {
        badge.classList.add('risk-high');
        badge.innerText = 'MODERATE RISK';
        sysMsg.innerText = 'Slight deviations from standard behavioral baseline. Monitor account.';
        meterFill.style.background = '#3B82F6';
        meterFill.style.width = '35%';
        meterFill.style.boxShadow = '0 0 20px #3B82F6';
    } else {
        badge.classList.add('risk-safe');
        badge.innerText = 'TRANSACTION SAFE';
        sysMsg.innerText = 'Transaction parameters aligned with authentic behavioral profiles.';
        meterFill.style.background = '#10B981';
        meterFill.style.width = '5%';
        meterFill.style.boxShadow = '0 0 20px #10B981';
    }
}

// Function to reset the scanner UI for the next transaction
window.resetScanner = function() {
    const radarContainer = document.getElementById('radar');
    const resultDisplay = document.getElementById('resultDisplay');
    const btnScan = document.querySelector('.btn-scan');
    const meterFill = document.getElementById('meterFill');

    resultDisplay.classList.add('hidden');
    radarContainer.classList.remove('hidden');
    
    btnScan.disabled = false;
    btnScan.innerHTML = '<span>Analyze Transaction</span><i data-feather="zap"></i>';
    feather.replace();
    
    // Reset meter
    meterFill.style.width = '0%';
    document.getElementById('probabilityText').innerText = '0.0%';
}

// Smooth Number Counter Animation
function animateValue(obj, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        obj.innerHTML = (progress * (end - start) + start).toFixed(1) + "%";
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}
