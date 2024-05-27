// let chatName=''
// let chatSocket = null
// let chatWindowUrl = window.location.href
// let chatRoomUuid= Math.random().toString(36).slice(2,12)

// console.log('chatRoomUid',chatRoomUuid);

// const chatElements = document.querySelector('#chat')
// const chatOpenElement = document.querySelector('#chat_open')
// const chatJoinElement = document.querySelector('#chat_join')
// const chatIconElement = document.querySelector('#chat_icon')
// const chatWelcomeElement = document.querySelector('#chat_welcome')
// const chatRoomElement = document.querySelector('#chat_room')

// console.log({
//     chatElements,
//     chatOpenElement,
//     chatJoinElement,
//     chatIconElement,
//     chatWelcomeElement,
// });

// chatOpenElement.onclick = function (e) {
//     e.preventDefault()
// console.log(chatIconElement);
//     chatIconElement.classList.add('hidden')
//     chatOpenElement.classList.remove('hidden')

//     return false

// }

// chatJoinElement.onclick = function (e) {
//     e.preventDefault()

//     chatWelcomeElement.classList.add('hidden')
//     chatRoomElement.classList.remove('hidden')

//     return false
// }

document.addEventListener("DOMContentLoaded", function () {
  let chatName = "";
  let chatSocket = null;
  let chatWindowUrl = window.location.href;
  let chatRoomUuid = Math.random().toString(36).slice(2, 12);

  console.log("chatRoomUid", chatRoomUuid);

  const chatElements = document.querySelector("#chat");
  const chatOpenElement = document.querySelector("#chat_open");
  const chatJoinElement = document.querySelector("#chat_join");
  const chatIconElement = document.querySelector("#chat_icon");
  const chatWelcomeElement = document.querySelector("#chat_welcome");
  const chatRoomElement = document.querySelector("#chat_room");
  const chatNameElement = document.querySelector("#chat_name");
  const chatLogElement = document.querySelector("#chat_log");
  const chatInputElement = document.querySelector("#chat_message_input");
  const chatSubmitElement = document.querySelector("#chat_message_submit");

  console.log({
    chatElements,
    chatOpenElement,
    chatJoinElement,
    chatIconElement,
    chatWelcomeElement,
  });

  function getCookie(name) {
    let cookieValue = null;
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();

      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }

    return cookieValue;
  }

  function sendMessage() {
    console.log("onsubmit");

    chatSocket.send(
      JSON.stringify({
        type: "message",
        message: chatInputElement.value,
        name: chatName,
      })
    );

    chatInputElement.value = "";
  }

  function onChatMessage(data) {
    console.log("onChatMessage", data);

    if (data.type == "chat_message") {
      if (data.agent) {
        chatLogElement.innerHTML += `
        <div class='flex w-full mt-2 space-x-3 max-w-md'> 
        <div class='flex-shrink-o h-10 w-10 rounded-full bg-gray-300 text-center pt-2'>
        ${data.initials}
    </div>
            <div>
                <div class = 'bg-gray-300 p-3 rounded-l-lg rounded-br-lg'>
                     <p class='text-sm'>${data.message}</p>
                </div>
                <span class='text-cs text-gray-500 leading-none'>${data.created_at} ago</span>
            </div>

        </div>`;
      } else {
        chatLogElement.innerHTML += `
                <div class='flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end'> 
                    <div>
                        <div class = 'bg-blue-300 p-3 rounded-l-lg rounded-br-lg'>
                             <p class='text-sm'>${data.message}</p>
                        </div>
                        <span class='text-cs text-gray-500 leading-none'>${data.created_at} ago</span>
                    </div>
                    <div class='flex-shrink-o h-10 w-10 rounded-full bg-gray-300 text-center pt-2'>
                        ${data.initials}
                    </div>
                </div>`;
      }
    }
  }

  async function joinChatRoom() {
    console.log("joinChatRoom");

    chatName = chatNameElement.value;

    console.log("Join as", chatName);
    console.log("url", chatWindowUrl);

    const data = new FormData();
    data.append("name", chatName);
    data.append("url", chatWindowUrl);
    const csrfToken = getCookie("csrftoken");
    await fetch(`/api/create-room/${chatRoomUuid}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": csrfToken,
      },
      body: data,
    })
      .then(function (res) {
        return res.json();
      })
      .then(function (data) {
        console.log("data", data);
      });

    chatSocket = new WebSocket(
      `ws://${window.location.host}/ws/${chatRoomUuid}/`
    );

    chatSocket.onmessage = function (e) {
      console.log("message");
      onChatMessage(JSON.parse(e.data));
    };

    chatSocket.onopen = function (e) {
      console.log("onOpen - chat socket was opened");
    };
    chatSocket.onclose = function (e) {
      console.log("onClose - chat socket was closed");
    };
  }

  if (chatOpenElement) {
    chatOpenElement.onclick = function (e) {
      e.preventDefault();
      console.log(chatIconElement);
      chatIconElement.classList.add("hidden");
      chatWelcomeElement.classList.remove("hidden");
    };
  } else {
    console.error("chatOpenElement is null");
  }

  if (chatJoinElement) {
    chatJoinElement.onclick = function (e) {
      e.preventDefault();
      chatWelcomeElement.classList.add("hidden");
      chatRoomElement.classList.remove("hidden");

      joinChatRoom();
    };
  } else {
    console.error("chatJoinElement is null");
  }

  chatSubmitElement.onclick = function (e) {
    e.preventDefault();
    console.log("onsubmit");
    sendMessage();
    return false;
  };
});
