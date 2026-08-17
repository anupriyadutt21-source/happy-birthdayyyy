import streamlit as st
import os

st.set_page_config(
    page_title="Happy Birthday Veduuu ❤️",
    page_icon="🎂",
    layout="wide"
)

# ============================================================
# FIND THE APP FOLDER
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# PAGE STYLE
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Great+Vibes&family=Poppins:wght@300;400;500;600&display=swap');

.stApp {
    background: linear-gradient(135deg, #120b12, #321323, #120b12);
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
    font-family: "Great Vibes", cursive;
    font-size: 100px;
    color: #ffb7d1;
    text-shadow: 0 0 30px rgba(255,105,180,0.5);
}

.subtitle {
    text-align: center;
    font-family: "Cormorant Garamond", serif;
    font-size: 30px;
    color: #ffd5e3;
}

.small-title {
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 4px;
    color: #ffc4da;
    font-size: 13px;
}

.section-heading {
    text-align: center;
    font-family: "Great Vibes", cursive;
    font-size: 65px;
    color: #ffd0df;
}

.section-title {
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 4px;
    color: #ffc4da;
    font-size: 12px;
    margin-top: 70px;
}

.description {
    text-align: center;
    color: #c9adb8;
}

.caption {
    text-align: center;
    font-family: "Great Vibes", cursive;
    font-size: 24px;
    color: white;
    margin-bottom: 30px;
}

.letter {
    max-width: 850px;
    margin: 40px auto;
    background: #fffaf7;
    color: #49353c;
    padding: 55px;
    border-radius: 12px;
    font-family: "Cormorant Garamond", serif;
    font-size: 20px;
    line-height: 1.7;
}

.poem {
    text-align: center;
    color: #7b4a5b;
    font-style: italic;
    margin: 30px 0;
}

.special {
    text-align: center;
    color: #b14d76;
    font-size: 28px;
    font-weight: bold;
}

.signature {
    text-align: center;
    font-family: "Great Vibes", cursive;
    color: #b14d76;
    font-size: 35px;
}

.ending {
    text-align: center;
    padding: 100px 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="small-title">A little birthday surprise for</div>',
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
    '<div class="subtitle">Happy Birthday, birthday boy 🎂</div>',
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# LETTER BUTTON
# ============================================================

if "open_letter" not in st.session_state:
    st.session_state.open_letter = False

if st.button("💌 Open Your Letter", use_container_width=True):

    st.session_state.open_letter = True
    st.balloons()


# ============================================================
# MUSIC
# ============================================================

if st.session_state.open_letter:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#ffc4da;
            font-size:18px;
            margin:20px;
        ">
        🎵 Birthday song ❤️
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


# ============================================================
# MEMORIES
# ============================================================

st.markdown(
    '<div class="section-title">OUR LITTLE MEMORIES</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-heading">Moments I Want To Keep 🤍</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="description">A few little pieces of us that I want to remember forever.</div>',
    unsafe_allow_html=True
)

st.write("")


# ============================================================
# PHOTO NAMES
# ============================================================

photos = [
    ("Photo1.jpg.png", "One of my favourite memories ♡"),
    ("Photo2.jpg.png", "A moment worth remembering 🌷"),
    ("Photo3.jpg.png", "You + Me + Memories"),
    ("Photo4.jpg.png", "Another little piece of us 🤍"),
    ("Photo5.jpg.png", "Forever grateful for this moment"),
    ("Photo6.jpg.jpeg", "My favourite birthday boy ❤️")
]


# ============================================================
# FUNCTION TO FIND PHOTOS
# ============================================================

def find_photo(filename):

    # Location 1: same folder as app.py
    path1 = os.path.join(BASE_DIR, filename)

    if os.path.isfile(path1):
        return path1

    # Location 2: images folder
    path2 = os.path.join(BASE_DIR, "images", filename)

    if os.path.isfile(path2):
        return path2

    return None


# ============================================================
# DISPLAY PHOTOS
# ============================================================

columns = st.columns(3)

for i, (filename, caption) in enumerate(photos):

    image_path = find_photo(filename)

    with columns[i % 3]:

        if image_path:

            st.image(
                image_path,
                use_container_width=True
            )

            st.markdown(
                f'<div class="caption">{caption}</div>',
                unsafe_allow_html=True
            )

        else:

            st.error(
                f"❌ Photo not found: {filename}"
            )


# ============================================================
# LETTER
# ============================================================

if st.session_state.open_letter:

    st.markdown(
        '<div class="section-title">FROM MY HEART TO YOURS</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-heading">To My Veduuu ❤️</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="letter">

    <p>
    Happy Birthday to my favourite person, my comfort, my happiness,
    and one of the most beautiful chapters of my life. 🥹❤️
    </p>

    <p>
    I have been thinking about what to write for you because a simple
    "Happy Birthday" could never possibly hold everything I feel for you.
    </p>

    <p>
    So today, I want to put my heart into words.
    </p>

    <p>
    I want you to know how much you mean to me—not just today,
    but every single day.
    </p>

    <h2>A little poem for you… 🌷</h2>

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

    <h2>For the birthday boy… 🎂</h2>

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
    Thank you for every laugh.
    </p>

    <p>
    Thank you for every conversation.
    </p>

    <p>
    Thank you for every memory.
    </p>

    <p>
    Thank you for every little effort.
    </p>

    <p>
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

    <h2>One last little piece for you… 🌷</h2>

    <div class="poem">

    If someday the years pass by,<br>
    and life takes us somewhere new,<br>
    I hope when you think of happiness,<br>
    one little memory leads to you.<br><br>

    I hope you remember the laughter,<br>
    the silly things we used to say,<br>
    the countless little moments,<br>
    that quietly made our days.<br><br>

    And if someone asks you someday,<br>
    "What made that time so sweet?"<br>
    I hope you smile just a little,<br>
    and remember the hearts that used to meet. ❤️

    </div>

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
    """, unsafe_allow_html=True)


# ============================================================
# END
# ============================================================

if st.session_state.open_letter:

    st.markdown("""
    <div class="ending">

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

    <p style="color:#d9bdc8;font-size:18px;">
    May this year bring you beautiful memories,
    happiness, success and countless reasons to smile. 🌷
    </p>

    <div style="font-size:45px;">
    🌷 🌷 🌷
    </div>

    </div>
    """, unsafe_allow_html=True)