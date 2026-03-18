let currentStep = 0;
const steps = document.querySelectorAll(".step");
const progress = document.getElementById("progress");
let startX = 0;

function showStep(index) {
    steps.forEach((step, i) => {
        step.classList.toggle("active", i === index);
    });

    const percent = ((index + 1) / steps.length) * 100;
    progress.style.width = percent + "%";
}

function nextStep() {
    const currentSelect = steps[currentStep].querySelector("select");

    if (currentSelect && currentSelect.value === "") {
        alert("Please select an option first.");
        return;
    }

    if (currentStep < steps.length - 1) {
        currentStep++;
        showStep(currentStep);
    }
}

function prevStep() {
    if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
    }
}

function toggleTheme() {
    document.body.classList.toggle("light-mode");
}

function resetQuiz() {
    const form = document.getElementById("quizForm");
    form.reset();
    currentStep = 0;
    showStep(currentStep);
}

document.addEventListener("touchstart", (e) => {
    startX = e.touches[0].clientX;
});

document.addEventListener("touchend", (e) => {
    let endX = e.changedTouches[0].clientX;

    if (startX - endX > 60) {
        nextStep();
    } else if (endX - startX > 60) {
        prevStep();
    }
});

showStep(currentStep);