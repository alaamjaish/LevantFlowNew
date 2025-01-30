// main.js

// Select DOM elements
const themeToggleButton = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');

// Load saved theme from localStorage
const savedTheme = localStorage.getItem('theme') || 'light';
if (savedTheme === 'dark') {
    document.body.classList.add('dark-mode');
    themeIcon.classList.remove('fa-moon');
    themeIcon.classList.add('fa-sun');
}

// Event listener for theme toggle
themeToggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
        localStorage.setItem('theme', 'dark');
    } else {
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
        localStorage.setItem('theme', 'light');
    }
});

// main.js

// Existing Dark Mode Code...

// Emoji Picker Integration
const emojiButton = document.getElementById('emoji-button');
const userInput = document.getElementById('user-input');

// Initialize Emoji Picker
const picker = new EmojiButton.EmojiButton();

// Show emoji picker when emoji button is clicked
emojiButton.addEventListener('click', () => {
    picker.togglePicker(emojiButton);
});

// Insert selected emoji into the input field
picker.on('emoji', emoji => {
    userInput.value += emoji;
    userInput.focus();
});