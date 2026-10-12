import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anitha ❤️",
    page_icon="💖",
    layout="centered"
)

# -------------------- CSS STYLING --------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #ffe1eb, #fff0f5, #f8d5ff);
}

.main .block-container {
    max-width: 700px;
    padding-top: 2rem;
    padding-bottom: 3rem;
    text-align: center;
}

h1, h2, h3, p {
    color: #a51c50;
}

.poem {
    background: rgba(255,255,255,0.82);
    border: 1px solid #ffc0d5;
    border-radius: 22px;
    padding: 22px 15px;
    margin: 18px 0;
    box-shadow: 0 5px 18px rgba(210,70,130,0.10);
    color: #a51c50;
    font-size: 18px;
    line-height: 1.9;
}

.english {
    color: #bd4775;
    font-size: 15px;
    font-style: italic;
}

.stButton > button {
    background: linear-gradient(135deg, #ff4d88, #e91e63);
    color: white;
    border: none;
    border-radius: 30px;
    padding: 14px 22px;
    font-size: 17px;
    font-weight: bold;
    width: 100%;
    transition: 0.3s;
    box-shadow: 0 5px 15px rgba(220, 40, 100, 0.2);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #d92768, #ad1457);
    color: white;
    border: none;
    transform: scale(1.02);
}

.rose-box {
    background: linear-gradient(135deg, #fff0f5, #ffe0eb, #fce4ec);
    border: 2px solid #ff8fb3;
    border-radius: 25px;
    padding: 25px 15px;
    margin: 22px 0;
    box-shadow: 0 8px 25px rgba(220, 20, 90, 0.16);
    text-align: center;
}

.rose-title {
    color: #c2185b;
    font-size: 23px;
    font-weight: bold;
}

.rose-icon {
    font-size: 65px;
    animation: rosePulse 1.5s infinite;
}

@keyframes rosePulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.15); }
}

.love-message {
    background: rgba(255, 255, 255, 0.85);
    border: 2px solid #ff8fb3;
    border-radius: 25px;
    padding: 25px 15px;
    margin: 20px 0;
    box-shadow: 0 5px 25px rgba(220, 20, 90, 0.16);
    color: #e6005c;
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    animation: loveAppear 1.2s ease-in-out;
}

@keyframes loveAppear {
    from {
        opacity: 0;
        transform: scale(0.5);
    }
    to {
        opacity: 1;
        transform: scale(1);
    }
}

.stCaption {
    color: #bd4775;
}
</style>
""", unsafe_allow_html=True)


# -------------------- FLOATING HEARTS --------------------

components.html("""
<div style="height:80px; overflow:hidden; position:relative;">
<style>
.heart {
    position:absolute;
    bottom:-40px;
    font-size:25px;
    animation:floatHeart 6s linear infinite;
}

@keyframes floatHeart {
    0% {
        transform:translateY(0) rotate(0deg);
        opacity:0;
    }
    20% { opacity:1; }
    100% {
        transform:translateY(-110px) rotate(35deg);
        opacity:0;
    }
}
</style>

<div class="heart" style="left:8%">💗</div>
<div class="heart" style="left:25%;animation-delay:2s">💕</div>
<div class="heart" style="left:45%;animation-delay:1s">💖</div>
<div class="heart" style="left:65%;animation-delay:3s">💘</div>
<div class="heart" style="left:85%;animation-delay:1.5s">❤️</div>
</div>
""", height=80)


# -------------------- INTRODUCTION --------------------

st.markdown("# 💖 Anitha!")
st.markdown("### 🌹 EN Thangamea Chellamea!")
st.markdown("### Who am I, if not yours? 🫶")

st.write("""
Ippothiku nan yarukittayum solla mudiyatha beautiful secret nee ❤️

Nee nu vanthu vitta ennaku love panna mattum tha theriyum.
""")

st.markdown("---")


# -------------------- FIRST LOVE POEM --------------------

st.markdown("## 🌷 உனக்காக ஒரு சின்ன கவிதை")

st.markdown("""
<div class="poem">
உன் சிரிப்பில் என் சந்தோஷம்,<br>
உன் பார்வையில் ஒரு மாயம்,<br>
நீ பேசும் ஒவ்வொரு வார்த்தையிலும்<br>
என் மனதிற்குள் ஆயிரம் ராகம்! 💗

<br><br>

Kadhal endrea theriyamal naa mulusa
love pannathu unnathan ❤️
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# -------------------- LOVE MESSAGE --------------------

st.markdown("## 🥹 Do You Know Something, Thango?")

st.write("""
Except u, enkitta irukkara ellam unakku than. ❤️

Unkitta pesurathu than good part of my day 🌹

Nee oru just person illa en life la.
You are someone who makes life feel more special. 💖

One thing... reason lam kekatha yen nu!!

Loving you, will love you... avalothan, chellam. 🫶
""")

st.markdown("""
<div class="poem">
நிலவுக்குக் கூடப் பொறாமை வரும்,<br>
உன் முகத்தைப் பார்த்தால்... 🌙

<br><br>

Nee pirakkum pothu unga appa rasichatha vida,
unna naan romba rasikkiren.

Enna panna ahh... unnai rasikkama irukka
than manasu illa! 🥹❤️
</div>
""", unsafe_allow_html=True)

st.markdown("---")


# -------------------- FIRST SURPRISE --------------------

st.markdown("## 💝 One Tiny Secret...")

if st.button("💌 Open Your Special Surprise ❤️", key="first_surprise"):
    st.balloons()

    st.markdown("""
    <div class="love-message">
        💖 Anitha, You Are My Favourite Notification!
        <br><br>
        <span style="font-size:18px;font-weight:normal;">
            Even a small message from u makes me smile. 🥹
            <br><br>
            If I could choose someone to make beautiful
            memories with, I would love to make those
            memories only with u, thango. 🌷
            <br><br>
            <b>You make my world a little more beautiful. 🌎💗</b>
        </span>
    </div>
    """, unsafe_allow_html=True)

    components.html("""
    <div id="surprise-hearts"
         style="position:fixed;inset:0;pointer-events:none;
                overflow:hidden;z-index:999999;">
    </div>

    <script>
    const box = document.getElementById('surprise-hearts');
    const symbols = ['💗','💕','💖','💘','❤️','🌸'];

    for (let i = 0; i < 45; i++) {
        const el = document.createElement('div');
        el.innerText = symbols[Math.floor(Math.random() * symbols.length)];
        el.style.cssText = `
            position:absolute;
            left:${Math.random() * 100}%;
            top:-40px;
            font-size:${18 + Math.random() * 22}px;
            animation:surpriseFall ${3 + Math.random() * 4}s
                       linear ${Math.random() * 2}s forwards;
        `;
        box.appendChild(el);
    }

    const css = document.createElement('style');
    css.innerHTML = `
        @keyframes surpriseFall {
            to {
                transform:translateY(110vh) rotate(540deg);
                opacity:0;
            }
        }
    `;
    document.head.appendChild(css);
    </script>
    """, height=0)

st.markdown("---")


# -------------------- CLICKABLE ROSE SURPRISE --------------------

st.markdown("## 🌹 A Rose Just For You")

st.markdown("""
<div class="rose-box">
    <div class="rose-icon">🌹</div>
    <div class="rose-title">
        A Little Rose For My Thangamea 💗
    </div>
    <p style="color:#bd4775;">
        Oru chinna rose... aana athukulla
        niraya love irukku! 🥹
    </p>
    <p style="color:#a51c50;">
        This rose is only for you, my chellam. 🌷
        <br>
    </p>
</div>
""", unsafe_allow_html=True)

if st.button("🌹 Click Here, Thangamea ❤️", key="rose_surprise"):
    st.session_state["rose_opened"] = True

if st.session_state.get("rose_opened", False):

    st.balloons()

    st.markdown("""
    <div class="love-message">
        🌹 LOVE YOU Thangamea ❤️
        <br><br>
        <span style="font-size:20px;font-weight:normal;">
            💗 💕 💖 💘 💝 💗 💕
            <br><br>
            En chellame, nee than en happiness! 🫶
            <br><br>
            Unna romba love panren di! 🥹❤️
            <br><br>
            Nee eppovume en special person! 🌹
            <br><br>
            <span style="font-size:16px;font-style:italic;">
                En heart la unakku mattum than special place,
                Anitha. ❤️
            </span>
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Rose petals and hearts falling across the screen
    components.html("""
    <div id="petal-container"
         style="position:fixed;inset:0;pointer-events:none;
                overflow:hidden;z-index:999999;">
    </div>

    <script>
    const container = document.getElementById('petal-container');
    const symbols = [
        '🌹','🌸','🌺','💗','💕','💖',
        '❤️','🌷','💘','💝','🌹','💞'
    ];

    for (let i = 0; i < 100; i++) {
        const petal = document.createElement('div');

        petal.innerText =
            symbols[Math.floor(Math.random() * symbols.length)];

        petal.style.position = 'absolute';
        petal.style.left = Math.random() * 100 + '%';
        petal.style.top = '-60px';
        petal.style.fontSize = (18 + Math.random() * 26) + 'px';
        petal.style.opacity = '0.95';
        petal.style.willChange = 'transform, opacity';

        petal.style.animation =
            'petalFall ' + (4 + Math.random() * 5) +
            's linear ' + (Math.random() * 4) + 's forwards';

        container.appendChild(petal);
    }

    const style = document.createElement('style');

    style.innerHTML = `
        @keyframes petalFall {
            0% {
                transform: translate3d(0, -5vh, 0) rotate(0deg);
                opacity: 1;
            }
            50% {
                transform:
                    translate3d(35px, 50vh, 0) rotate(360deg);
                opacity: 1;
            }
            100% {
                transform:
                    translate3d(-30px, 115vh, 0) rotate(720deg);
                opacity: 0;
            }
        }
    `;

    document.head.appendChild(style);
    </script>
    """, height=0)

st.markdown("---")


# -------------------- FINAL LOVE LETTER --------------------

st.markdown("## 🌹 One Last Thing, Anitha...")

st.markdown("""
<div class="poem">

Unna yen pidichirukunu reason thedunen... ❤️

Last ahh tha purinjathu,
antha reason ye nee than, chello! 🥹

<br><br>

Na unna unga appa alavuko,
yen unakku pidicha thambi alavuko,
seri Arun alavuko nesikka mudiyuma nu therla, thango...
But onnu soldren...<br>
             ivagala nee thedatha alavuku ennala unna neneasikka mudyium. ❤️

<br><br>

<span class="english">
U r the most beautiful part of my day,<br>
And the sweetest poem my heart could ever say. ❤️
</span>

<br><br>

💗 Forever my special person, Anitha. 🌹

</div>
""", unsafe_allow_html=True)


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown("""
<p style="text-align:center;color:#bd4775;font-size:16px;">
Made with endless love, especially for Anitha ❤️
<br>
🌹 💗 💕 💖 💕 💗 🌹
</p>
""", unsafe_allow_html=True)