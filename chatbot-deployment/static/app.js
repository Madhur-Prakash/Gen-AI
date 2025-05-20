class Chatbot{  
    constructor(){
        this.args={
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }
        this.state= false;
        this.message=[];
    }
    display(){
        const {openButton, chatBox, sendButton}=this.args;
        openButton.addEventListener('click', ()=>this.toggleState(chatBox));
        sendButton.addEventListener('click', ()=>this.onSendButton(chatBox));
        const node=chatBox.querySelector('input');
        node.addEventListener('keydown', (e)=> {
            if(e.key==='Enter'){
                this.onSendButton(chatBox);
            }
        })
    }
    toggleState(chatBox){
        this.state = !this.state;
        if(this.state){
            chatBox.classList.add('chatbox--active');
        }else{
            chatBox.classList.remove('chatbox--active');
        }
    }
    onSendButton(chatBox){
        const messageInput = chatBox.querySelector('input');
        const message = messageInput.value.trim();
        if(message){
            this.message.push(message);
            messageInput.value = '';
        }
    }

onSendButton(chatBox){
    const messageInput = chatBox.querySelector('input');
    const message = messageInput.value.trim();
    if(message){
        this.message.push(message);
        messageInput.value = '';
    }

}}