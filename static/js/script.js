// Ayurveda Website - Chatbot JavaScript

const sessionId = generateSessionId();

// Generate unique session ID
function generateSessionId() {
    return 'session_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

// Initialize chatbot
document.addEventListener('DOMContentLoaded', function() {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const clearButton = document.getElementById('clearButton');

    if (sendButton) {
        sendButton.addEventListener('click', sendMessage);
    }

    if (messageInput) {
        messageInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
            }
        });
    }

    if (clearButton) {
        clearButton.addEventListener('click', clearChat);
    }

    // Load initial greeting
    addBotMessage("🙏 Namaste! I'm your Ayurveda assistant. Ask me anything about Ayurvedic principles, nutrition, health conditions, or wellness practices. How can I help you today?");
});

// Send message to chatbot
async function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messagesContainer = document.getElementById('messagesContainer');
    const message = messageInput.value.trim();

    if (!message) return;

    // Add user message to chat
    addUserMessage(message);
    messageInput.value = '';
    messageInput.focus();

    // Show loading indicator
    const loadingId = addLoadingMessage();

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Remove loading indicator
        removeMessage(loadingId);

        if (data.response) {
            addBotMessage(data.response);
        } else if (data.error) {
            addBotMessage(`❌ Error: ${data.error}`);
        }
    } catch (error) {
        console.error('Error:', error);
        removeMessage(loadingId);
        addBotMessage(`❌ Sorry, I encountered an error: ${error.message}. Please try again.`);
    }

    // Auto-scroll to bottom
    if (messagesContainer) {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }
}

// Add user message to chat
function addUserMessage(text) {
    const messagesContainer = document.getElementById('messagesContainer');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    messageDiv.innerHTML = `<div class="text">${escapeHtml(text)}</div>`;
    messagesContainer.appendChild(messageDiv);
}

// Add bot message to chat
function addBotMessage(text) {
    const messagesContainer = document.getElementById('messagesContainer');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant';
    messageDiv.innerHTML = `<div class="text">${formatText(text)}</div>`;
    const id = 'msg_' + Date.now();
    messageDiv.id = id;
    messagesContainer.appendChild(messageDiv);
    return id;
}

// Add loading message
function addLoadingMessage() {
    const messagesContainer = document.getElementById('messagesContainer');
    const messageDiv = document.createElement('div');
    const id = 'loading_' + Date.now();
    messageDiv.id = id;
    messageDiv.className = 'message assistant';
    messageDiv.innerHTML = `<div class="text"><div class="loading"></div> Thinking...</div>`;
    messagesContainer.appendChild(messageDiv);
    return id;
}

// Remove message by ID
function removeMessage(id) {
    const element = document.getElementById(id);
    if (element) {
        element.remove();
    }
}

// Clear chat
async function clearChat() {
    if (confirm('Are you sure you want to clear the chat history?')) {
        try {
            const response = await fetch('/api/clear-chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    session_id: sessionId
                })
            });

            if (response.ok) {
                const messagesContainer = document.getElementById('messagesContainer');
                messagesContainer.innerHTML = '';
                addBotMessage("🙏 Chat cleared! Namaste! How can I assist you with Ayurveda and nutrition today?");
            }
        } catch (error) {
            console.error('Error clearing chat:', error);
            alert('Failed to clear chat');
        }
    }
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, m => map[m]);
}

// Format text with markdown-like features
function formatText(text) {
    // Escape HTML first
    let formatted = escapeHtml(text);

    // Convert line breaks
    formatted = formatted.replace(/\n/g, '<br>');

    // Bold text **text**
    formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Italic text *text*
    formatted = formatted.replace(/\*(.*?)\*/g, '<em>$1</em>');

    // Code blocks
    formatted = formatted.replace(/`(.*?)`/g, '<code style="background-color: #f0f0f0; padding: 2px 6px; border-radius: 3px;">$1</code>');

    // Lists
    formatted = formatted.replace(/• (.*?)(<br>|$)/g, '&bull; $1<br>');

    return formatted;
}

// Add smooth scroll behavior
if ('scrollBehavior' in document.documentElement.style) {
    document.documentElement.style.scrollBehavior = 'smooth';
}
