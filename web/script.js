/* =========================
   COMMON PASSWORDS
========================= */

const COMMON_PASSWORDS = new Set([
    "password",
    "123456",
    "123456789",
    "12345678",
    "12345",
    "qwerty",
    "abc123",
    "password1",
    "admin",
    "admin123",
    "letmein",
    "welcome",
    "monkey",
    "dragon",
    "football",
    "iloveyou",
    "login",
    "princess",
    "qwerty123"
]);


/* =========================
   COMMON SEQUENCES
========================= */

const COMMON_SEQUENCES = [
    "1234",
    "12345",
    "123456",
    "abcd",
    "abcde",
    "abcdef",
    "qwerty",
    "qwert",
    "asdf",
    "zxcv",
    "9876"
];


/* =========================
   GET HTML ELEMENTS
========================= */

const passwordInput = document.getElementById("password");

const analyzeButton = document.getElementById("analyzeButton");

const togglePassword = document.getElementById("togglePassword");

const results = document.getElementById("results");


/* =========================
   PASSWORD VISIBILITY
========================= */

togglePassword.addEventListener("click", function () {

    if (passwordInput.type === "password") {

        passwordInput.type = "text";

        togglePassword.textContent = "🙈";

    } else {

        passwordInput.type = "password";

        togglePassword.textContent = "👁️";

    }

});


/* =========================
   REPEATED CHARACTER CHECK
========================= */

function checkRepeatedCharacters(password) {

    for (let i = 0; i < password.length - 2; i++) {

        if (
            password[i] === password[i + 1] &&
            password[i] === password[i + 2]
        ) {

            return true;

        }

    }

    return false;

}


/* =========================
   SEQUENCE CHECK
========================= */

function checkSequences(password) {

    const lowerPassword = password.toLowerCase();

    for (const sequence of COMMON_SEQUENCES) {

        if (lowerPassword.includes(sequence)) {

            return true;

        }

    }

    return false;

}


/* =========================
   UPDATE CHECK CARD
========================= */

function updateCheck(id, passed, text) {

    const card = document.getElementById(id);

    const icon = card.querySelector(".check-icon");

    icon.textContent = passed ? "✅" : "❌";

    card.style.borderColor = passed
        ? "#bbf7d0"
        : "#fecaca";

    icon.style.background = passed
        ? "#f0fdf4"
        : "#fef2f2";

    const paragraph = card.querySelector("p");

    paragraph.textContent = text;

}


/* =========================
   ANALYZE PASSWORD
========================= */

function analyzePassword() {

    const password = passwordInput.value;

    if (password.length === 0) {

        alert("Please enter a password to analyze.");

        return;

    }


    /* =========================
       SECURITY CHECKS
    ========================= */

    const lengthPassed = password.length >= 8;

    const uppercasePassed = /[A-Z]/.test(password);

    const lowercasePassed = /[a-z]/.test(password);

    const numberPassed = /[0-9]/.test(password);

    const specialPassed = /[^A-Za-z0-9]/.test(password);

    const commonPassed =
        !COMMON_PASSWORDS.has(password.toLowerCase());

    const repeatedFound =
        checkRepeatedCharacters(password);

    const sequenceFound =
        checkSequences(password);


    /* =========================
       SCORE
    ========================= */

    let score = 0;


    if (lengthPassed) {
        score++;
    }

    if (uppercasePassed) {
        score++;
    }

    if (lowercasePassed) {
        score++;
    }

    if (numberPassed) {
        score++;
    }

    if (specialPassed) {
        score++;
    }


    /* =========================
       STRENGTH
    ========================= */

    let strength = "";
    let description = "";


    if (!commonPassed) {

        strength = "VERY WEAK";

        description =
            "This password is commonly used and should be avoided.";

    }

    else if (score <= 2) {

        strength = "WEAK";

        description =
            "This password needs significant improvement.";

    }

    else if (score === 3) {

        strength = "MODERATE";

        description =
            "This password has some good characteristics but can be improved.";

    }

    else if (score === 4) {

        strength = "STRONG";

        description =
            "This password has several strong security characteristics.";

    }

    else {

        strength = "VERY STRONG";

        description =
            "This password meets all of the basic checks.";

    }


    /* =========================
       DISPLAY SCORE
    ========================= */

    document.getElementById("score").textContent = score;

    document.getElementById("strength").textContent = strength;

    document.getElementById("strengthDescription").textContent =
        description;


    /* =========================
       DISPLAY CHECKS
    ========================= */

    updateCheck(
        "lengthCheck",
        lengthPassed,
        lengthPassed
            ? "At least 8 characters."
            : "Use at least 8 characters."
    );


    updateCheck(
        "uppercaseCheck",
        uppercasePassed,
        uppercasePassed
            ? "Contains an uppercase letter."
            : "Add an uppercase letter."
    );


    updateCheck(
        "lowercaseCheck",
        lowercasePassed,
        lowercasePassed
            ? "Contains a lowercase letter."
            : "Add a lowercase letter."
    );


    updateCheck(
        "numberCheck",
        numberPassed,
        numberPassed
            ? "Contains a number."
            : "Add at least one number."
    );


    updateCheck(
        "specialCheck",
        specialPassed,
        specialPassed
            ? "Contains a special character."
            : "Add a special character."
    );


    updateCheck(
        "commonCheck",
        commonPassed,
        commonPassed
            ? "Not found in the common-password list."
            : "This is a commonly used password."
    );


    updateCheck(
        "repeatCheck",
        !repeatedFound,
        !repeatedFound
            ? "No obvious repeated characters."
            : "Contains repeated characters."
    );


    updateCheck(
        "sequenceCheck",
        !sequenceFound,
        !sequenceFound
            ? "No obvious simple sequence detected."
            : "Contains a simple sequence."
    );


    /* =========================
       RECOMMENDATIONS
    ========================= */

    const recommendationsList =
        document.getElementById("recommendationsList");

    recommendationsList.innerHTML = "";


    const recommendations = [];


    if (!lengthPassed) {

        recommendations.push(
            "Use a longer password. Aim for at least 12 characters."
        );

    }


    if (!uppercasePassed) {

        recommendations.push(
            "Add uppercase letters."
        );

    }


    if (!lowercasePassed) {

        recommendations.push(
            "Add lowercase letters."
        );

    }


    if (!numberPassed) {

        recommendations.push(
            "Add numbers."
        );

    }


    if (!specialPassed) {

        recommendations.push(
            "Add special characters such as !, @, #, or $."
        );

    }


    if (!commonPassed) {

        recommendations.push(
            "Avoid common passwords and predictable words."
        );

    }


    if (repeatedFound) {

        recommendations.push(
            "Avoid repeating the same character multiple times."
        );

    }


    if (sequenceFound) {

        recommendations.push(
            "Avoid simple sequences such as 1234, abcd, or qwerty."
        );

    }


    if (recommendations.length === 0) {

        recommendations.push(
            "Great job! Your password passes all of the basic checks."
        );

        recommendations.push(
            "For real accounts, consider using a password manager and unique passwords."
        );

    }


    for (const recommendation of recommendations) {

        const li = document.createElement("li");

        li.textContent = recommendation;

        recommendationsList.appendChild(li);

    }


    /* =========================
       SHOW RESULTS
    ========================= */

    results.classList.remove("hidden");


    results.scrollIntoView({
        behavior: "smooth"
    });

}


/* =========================
   BUTTON EVENT
========================= */

analyzeButton.addEventListener(
    "click",
    analyzePassword
);


/* =========================
   ENTER KEY
========================= */

passwordInput.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Enter") {

            analyzePassword();

        }

    }
);