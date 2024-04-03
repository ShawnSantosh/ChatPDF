css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://e7.pngegg.com/pngimages/498/917/png-clipart-computer-icons-desktop-chatbot-icon-blue-angle-thumbnail.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/png;base64,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">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
