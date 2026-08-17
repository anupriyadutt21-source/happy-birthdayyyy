import streamlit as st
import os

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Happy Birthday Veduuu ❤️",
    page_icon="❤️",
    layout="wide"
)

# ---------------- CSS ----------------

st.markdown(
    """
    <style>
    
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins:wght@300;400;500;600&display=swap');

    .stApp {
        background: linear-gradient(135deg, #160b13, #351525, #160b13);
        color: white;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }

    .title {
        text-align: center;
        font-family: 'Great Vibes', cursive;
        font-size: 100px;
        color: #ffb6d0;
        margin-top: 50px;
        text-shadow: 0 0 30px #ff6f9f;
    }

    .subtitle {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        color: #ffdce8;
        font-size: 22px;
    }

    .small {
        text-align: center;
        color: #e8b7c8;
        letter-spacing: 4px;
        text-transform: uppercase;
        font-size: 12px;
    }

    .section {
        text-align: center;
        font-family: 'Great Vibes', cursive;
        font-size: 60px;
        color: #ffd0df;
        margin-top: 80px;
    }

    .letter {
        background: #fffaf7;
        color: #49353c;
        padding: 45px;
        border-radius: 12px;
        max-width: 850px;
        margin: auto;
        font-family: Georgia, serif;
        font-size: 19px;
        line-height: 1.8;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }

    .poem {
        text-align: center;
        color: #9b5270;
        font-style: italic;
        margin: 35px 0;
    }

    .special {
        text-align: center;
        color: #b24e77;
        font-size: 28px;
        font-weight: bold;
    }

    .signature {
        text-align: center;
        color: #b24e77;
        font-family: 'Great Vibes', cursive;
        font-size: 35px;
    }

    .memory {
        background: white;
        padding: 10px 10px 20px 10px;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.5);
    }

    .caption {
        color: #613f4c;
        text-align: center;
        font-family: 'Great Vibes', cursive;
        font-size: 23px;
        margin-top: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- FLOATING HEARTS ----------------

st.markdown(
    """
    <div style="
        position:fixed;
        top:10%;
        left:8%;
        font-size:30px;
        opacity:0.3;
        z-index:0;
    ">♡</div>

    <div style="
        position:fixed;
        top:30%;
        right:10%;
        font-size:25px;
        opacity:0.3;
        z-index:0;
    ">♥</div>

    <div style="
        position:fixed;
        bottom:20%;
        left:15%;
        font-size:25px;
        opacity:0.3;
        z-index:0;
    ">♡</div>

    <div style="
        position:fixed;
        bottom:10%;
        right:15%;
        font-size:30px;
        opacity:0.3;
        z-index:0;
    ">♥</div>
    """,
    unsafe_allow_html=True
)

# ---------------- HERO ----------------

st.markdown(
    '<p class="small">A little birthday surprise for</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">Veduuu</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="text-align:center;font-size:30px;">♡ ✦ ♡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Happy Birthday, birthday boy 🎂</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center;color:#dcb5c5;">Made with lots of love ❤️</p>',
    unsafe_allow_html=True
)

# ---------------- OPEN LETTER ----------------

if "open" not in st.session_state:
    st.session_state.open = False

if st.button("💌 Open Your Letter", use_container_width=True):

    st.session_state.open = True

    st.balloons()

# ---------------- YOUTUBE MUSIC ----------------

if st.session_state.open:

    st.markdown(
        """
        <div style="text-align:center;color:#ffc5d9;font-size:18px;">
        🎵 Your birthday song is playing ❤️
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <iframe
            width="1"
            height="1"
            src="https://www.youtube.com/embed/32YzafO9Bmo?autoplay=1&loop=1&playlist=32YzafO9Bmo"
            frameborder="0"
            allow="autoplay; encrypted-media">
        </iframe>
        """,
        unsafe_allow_html=True
    )

# ---------------- MEMORIES ----------------

st.markdown(
    '<div class="section">Our Little Memories 🤍</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="text-align:center;color:#cbaeba;">A few little pieces of us that I want to remember forever.</p>',
    unsafe_allow_html=True
)

photos = [
    ("Photo1.jpg.png", "One of my favourite memories ♡"),
    ("Photo2.jpg.png", "A moment worth remembering 🌷"),
    ("Photo3.jpg.png", "You + Me + Memories"),
    ("Photo4.jpg.png", "Another little piece of us 🤍"),
    ("Photo5.jpg.png", "Forever grateful for this moment"),
    ("Photo6.jpg.jpeg", "My favourite birthday boy ❤️")
]

columns = st.columns(3)

for i, (photo, caption) in enumerate(photos):

    with columns[i % 3]:

        if os.path.exists(photo):

            st.markdown('<div class="memory">', unsafe_allow_html=True)

            st.image(photo, use_container_width=True)

            st.markdown(
                f'<div class="caption">{caption}</div>',
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

        else:

            st.warning(f"{photo} not found")

# ---------------- LETTER ----------------

if st.session_state.open:

    st.markdown(
        '<div class="section">From My Heart To Yours ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="letter">

        <p>
        Happy Birthday to my favourite person, my comfort, my happiness,
        and one of the most beautiful chapters of my life. 🥹❤️
        </p>

        <p>
        I have been thinking about what to write for you because a simple
        “Happy Birthday” could never possibly hold everything I feel for you.
        </p>

        <p>
        So today, I want to put my heart into words.
        </p>

        <p>
        I want you to know how much you mean to me—not just today,
        but every single day.
        </p>

        <h2 style="text-align:center;color:#b24e77;">
        A little poem for you… 🌷
        </h2>

        <div class="poem">

        If I could gather every star,<br>
        and place them gently in your hands,<br>
        I'd still feel they were not enough,<br>
        to show you where my heart still stands.<br><br>

        If I could collect every flower,<br>
        and make the whole world bloom,<br>
        I'd still choose the smallest one,<br>
        if it reminded me of you.<br><br>

        And if the world gave me a thousand choices,<br>
        a thousand paths to walk through,<br>
        I'd still look for the same smile,<br>
        I'd still find my way to you. ❤️

        </div>

        <p>
        Veduuu, you became important to me in a way I never expected.
        </p>

        <p>
        Somewhere between our conversations, our laughs, our silly arguments,
        our random moments, and all the memories we've created,
        you became someone incredibly special to me.
        </p>

        <p>
        You became the person I want to tell things to.
        </p>

        <p>
        The person whose messages can make an ordinary day feel a little better.
        </p>

        <p>
        The person who can make me smile without even trying.
        </p>

        <p>
        And somehow, without even realizing it,
        <strong>you became my Veduuu. ❤️</strong>
        </p>

        <p>
        I love all the little things about us.
        </p>

        <p>
        The stupid conversations.<br>
        The random jokes.<br>
        The moments where neither of us makes any sense.<br>
        The times we annoy each other.<br>
        The times we laugh until our stomachs hurt.<br>
        The serious conversations.
        </p>

        <p>
        The little memories that probably seem ordinary to everyone else
        but mean everything to me.
        </p>

        <p>
        Those are the moments I want to keep forever.
        </p>

        <h2 style="text-align:center;color:#b24e77;">
        For the birthday boy… 🎂
        </h2>

        <div class="poem">

        May your dreams find their way to you,<br>
        may your worries slowly fade,<br>
        may every little hope you carry,<br>
        become a beautiful memory someday.<br><br>

        May life give you reasons to smile,<br>
        more than reasons to cry,<br>
        may you always believe in yourself,<br>
        even when the road feels high.<br><br>

        And if someday you forget your worth,<br>
        if life makes you doubt what you can do,<br>
        I hope you remember there is someone,<br>
        who will always believe in you. ❤️

        </div>

        <p>
        Today is your birthday, but honestly, I feel like I'm the lucky one.
        </p>

        <p>
        Because I got to meet you.
        </p>

        <p>
        I got to know you.
        </p>

        <p>
        I got to make memories with you.
        </p>

        <p>
        I got to experience all these little moments that became so precious to me.
        </p>

        <p>
        And for that, I will always be grateful.
        </p>

        <p>
        Thank you for every laugh.<br>
        Thank you for every conversation.<br>
        Thank you for every memory.<br>
        Thank you for every little effort.<br>
        Thank you for simply being <strong>you.</strong>
        </p>

        <p>
        You don't have to be perfect.
        </p>

        <p>
        You don't have to have everything figured out.
        </p>

        <p>
        You are allowed to have bad days.
        </p>

        <p>
        You are allowed to make mistakes.
        </p>

        <p>
        Just keep being yourself.
        </p>

        <p>
        Because the person you are right now is already someone worth
        appreciating and celebrating.
        </p>

        <p>
        And I hope you never forget that.
        </p>

        <p>
        My Veduuu,
        </p>

        <p>
        I don't know what every tomorrow will look like.
        </p>

        <p>
        I don't know what life has planned.
        </p>

        <p>
        But I know that <strong>today</strong>, I am incredibly grateful
        that you're a part of my life.
        </p>

        <p>
        On your birthday, more than anything, I want you to be happy.
        </p>

        <p>
        I want you to laugh.
        </p>

        <p>
        I want you to feel loved.
        </p>

        <p>
        I want you to feel proud of yourself.
        </p>

        <p>
        I want you to know that your existence matters.
        </p>

        <p>
        May you have beautiful beginnings.
        </p>

        <p>
        May you have unforgettable memories.
        </p>

        <p>
        May you find success.
        </p>

        <p>
        May you find peace.
        </p>

        <p>
        May you always have reasons to smile.
        </p>

        <p>
        And may you always remain the wonderful, silly, lovable
        <strong>Veduuu</strong> that I know. ❤️
        </p>

        <p class="special">
        Happy Birthday, my Veduuu. 🎂❤️
        </p>

        <p>
        I hope you know just how incredibly special you are to me.
        </p>

        <p class="special">
        Keep smiling. Keep dreaming. Keep being you. ❤️
        </p>

        <p class="signature">
        Your girl,<br>
        who loves her Veduuu more than words can ever properly explain. ❤️🌷
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- END ----------------

if st.session_state.open:

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:100px 20px;
        ">

        <div style="font-size:45px;">
        🤍 🌹 🤍 🌹 🤍
        </div>

        <div style="
            font-family:'Great Vibes',cursive;
            font-size:70px;
            color:#ffd0df;
        ">
        Happy Birthday, Veduuu ❤️
        </div>

        <p style="color:#d9bdc8;">
        May this year bring you beautiful memories,
        happiness, success and countless reasons to smile. 🌷
        </p>

        <div style="font-size:45px;">
        🌷 🌷 🌷
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )