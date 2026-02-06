from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)

# --- פונקציית עזר ללינקים ---
def make_map_link(query):
    encoded_query = urllib.parse.quote(query)
    return f"https://www.google.com/maps/search/?api=1&query={encoded_query}"

# --- נתוני התוכנית המלאה (6 ימים בבטומי) ---
def get_plan():
    plan = [
        {
            "day": 1,
            "title": "נחיתה, התארגנות וטבילת אש",
            "desc": "נוחתים, מתמקמים במגדלים ויוצאים לראות את העיר בערב.",
            "areas": [
                {
                    "name": "נחיתה והגעה ל-Orbi",
                    "time": "16:00 - 18:30",
                    "travel": "🚕 מונית (Yandex/Bolt בלבד)",
                    "desc": "יוצאים מהשדה, מזמינים מונית באפליקציה (כ-15 לארי) ישר למגדלים.",
                    "spots": [
                        {"name": "Orbi City", "desc": "צ'ק אין בדירה. שימו מזוודות ותרדו למטה.", "query": "Orbi City Batumi"},
                        {"name": "Willmart", "desc": "סופרמרקט ענק מתחת למלון. לקנות שישיות מים ונשנושים לחדר.", "query": "Willmart Orbi City"},
                        {"name": "Magti", "desc": "חנות סלולר ב-Batumi Mall (5 דק' הליכה). לעשות סים ואינטרנט.", "query": "Magti Batumi Mall"}
                    ]
                },
                {
                    "name": "Batumi Boulevard (הטיילת)",
                    "time": "19:00 - 23:30",
                    "travel": "🚶 הליכה ברגל",
                    "desc": "הלב של בטומי. הולכים לאורך הים, רואים את האורות ואוכלים.",
                    "spots": [
                        {"name": "Kiziki", "desc": "חובה! המסעדה הכי טובה לחצ'אפורי אג'רולי (סירה) וחינקלי.", "query": "Kiziki Restaurant Batumi"},
                        {"name": "פסל עלי ונינו", "desc": "הפסל המסתובב המפורסם. חובה לסטורי.", "query": "Ali and Nino Statue"},
                        {"name": "המזרקות הרוקדות", "desc": "מופע מים ואורות באגם ארדגאני (ליד הדירה).", "query": "Dancing Fountains Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 2,
            "title": "אדרנלין ונוף מלמעלה",
            "desc": "מתחילים במים ומשתזפים, ומסיימים בתצפית הכי יפה בעיר.",
            "areas": [
                {
                    "name": "פארק מים / חוף",
                    "time": "10:30 - 15:00",
                    "travel": "🚶 הליכה בטיילת",
                    "desc": "בוקר של בטן גב ואקשן.",
                    "spots": [
                        {"name": "Batumi Aqua Park", "desc": "פארק מים על הטיילת. מגלשות ובריכות.", "query": "Batumi Aqua Park"},
                        {"name": "Iveria Beach", "desc": "אם לא בא לכם מגלשות - זה מועדון חוף סטייל עם מוזיקה.", "query": "Iveria Beach Batumi"}
                    ]
                },
                {
                    "name": "רכבל ופיאצה",
                    "time": "16:30 - 22:00",
                    "travel": "🚕 מונית למרכז",
                    "desc": "עולים להר לתצפית שקיעה ויורדים לכיכר האיטלקית.",
                    "spots": [
                        {"name": "רכבל ארגו (Argo)", "desc": "רכבל ארוך שעולה לתצפית על כל העיר. שווה להגיע בשקיעה.", "query": "Argo Cable Car"},
                        {"name": "Piazza Square", "desc": "כיכר יפהפייה עם בתי קפה, הופעות חיות ושעון מנגן.", "query": "Piazza Square Batumi"},
                        {"name": "La Brioche", "desc": "מקום טוב בכיכר לקפה וקינוח בערב.", "query": "La Brioche Piazza Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 3,
            "title": "שופינג בזול ודולפינים",
            "desc": "יום שמוקדש לקניות בשוק הזול ולאטרקציות ימיות.",
            "areas": [
                {
                    "name": "Hopa Market (שוק הופה)",
                    "time": "10:00 - 13:30",
                    "travel": "🚕 מונית (כ-7 דק')",
                    "desc": "ה-מקום לקנות בגדים, נעליים וחיקויים בזול. תתמקחו על הכל!",
                    "spots": [
                        {"name": "Hopa Bazaar", "desc": "מתחם ענק של דוכנים. תבואו עם מזומן.", "query": "Hopa Market Batumi"},
                        {"name": "דוכני צ'ורצ'חלה", "desc": "לקנות ממתקים גאורגיים הביתה.", "query": "Hopa Market Batumi Food"}
                    ]
                },
                {
                    "name": "דולפינים ושיט",
                    "time": "14:30 - 18:00",
                    "travel": "🚕 חזרה לטיילת",
                    "desc": "חוזרים למרכז העניינים.",
                    "spots": [
                        {"name": "Batumi Dolphinarium", "desc": "מופע דולפינים מפורסם (להזמין כרטיס מראש!).", "query": "Batumi Dolphinarium"},
                        {"name": "נמל בטומי (שיט)", "desc": "ביציאה מהנמל יש סירות מנוע. סוגרים סיבוב של חצי שעה בים.", "query": "Batumi Yacht Club"}
                    ]
                },
                {
                    "name": "חיי לילה",
                    "time": "22:00 - אל הלילה",
                    "travel": "🚶 על החוף",
                    "desc": "המסיבות הכי טובות בעיר.",
                    "spots": [
                        {"name": "Sector 26", "desc": "מועדון פתוח עם בריכה. הכי חזק בקיץ.", "query": "Sector 26 Batumi"},
                        {"name": "Soho Batumi", "desc": "ממש ליד, אווירה קצת יותר יוקרתית.", "query": "Soho Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 4,
            "title": "הרים, מפלים ובאולינג",
            "desc": "יום יציאה מהעיר לטבע שנגמר בתחרות באולינג.",
            "areas": [
                {
                    "name": "שמורת מחונצטי (Makhuntseti)",
                    "time": "10:00 - 15:00",
                    "travel": "🚙 נהג צמוד (כ-50 דק' נסיעה)",
                    "desc": "יוצאים להרי אג'רה. ירוק בעיניים ומים.",
                    "spots": [
                        {"name": "מפל מחונצטי", "desc": "מפל גבוה ומרשים, אפשר להיכנס למים הקפואים.", "query": "Makhuntseti Waterfall"},
                        {"name": "גשר המלכה תמר", "desc": "גשר אבן עתיק וגבוה מעל הנהר.", "query": "Queen Tamar Bridge"},
                        {"name": "רפטינג", "desc": "יש בדרך נקודות לרפטינג בנהר (לא אקסטרים מדי, כיף).", "query": "Rafting Makhuntseti"}
                    ]
                },
                {
                    "name": "Adjarian Wine House",
                    "time": "15:30 - 17:30",
                    "travel": "🚙 בדרך חזרה",
                    "desc": "עצירה לאוכל במקום הכי יפה באזור.",
                    "spots": [
                        {"name": "בית היין האג'רי", "desc": "מסעדה בתוך יקב עתיק, אוכל מעולה ונוף לכרמים.", "query": "Adjarian Wine House"}
                    ]
                },
                {
                    "name": "באולינג ומשחקים",
                    "time": "19:00 - 22:00",
                    "travel": "🚕 מונית לקניון",
                    "desc": "סוגרים את הערב במזגן עם קצת תחרות.",
                    "spots": [
                        {"name": "Metro City Bowling", "desc": "מתחם באולינג ומשחקי וידאו בתוך הקניון.", "query": "Metro City Forum Batumi Bowling"},
                        {"name": "Food Court", "desc": "מקדונלדס/KFC או אוכל גאורגי בקניון.", "query": "Metro City Forum Food Court"}
                    ]
                }
            ]
        },
        {
            "day": 5,
            "title": "הגן הבוטני, קרטינג ויוקרה",
            "desc": "חוף צלול, אקשן על המסלול וארוחת ערב חגיגית.",
            "areas": [
                {
                    "name": "הכף הירוק (Mtsvane Kontskhi)",
                    "time": "10:30 - 15:30",
                    "travel": "🚕 מונית (כ-20 דק')",
                    "desc": "מקום חובה. יער שנופל לתוך הים.",
                    "spots": [
                        {"name": "הגן הבוטני", "desc": "מסלול הליכה (או נסיעה ברכב חשמלי) עם נוף משוגע.", "query": "Batumi Botanical Garden"},
                        {"name": "החוף הירוק", "desc": "החוף מתחת לגן. המים פה הרבה יותר נקיים מבטומי העיר.", "query": "Mtsvane Kontskhi Beach"}
                    ]
                },
                {
                    "name": "קרטינג בטומי",
                    "time": "16:30 - 18:30",
                    "travel": "🚕 חזרה לעיר",
                    "desc": "מעלים דופק לפני הערב.",
                    "spots": [
                        {"name": "Batumi Karting", "desc": "מסלול קרטינג גדול ומקצועי על הטיילת החדשה.", "query": "Karting Batumi"}
                    ]
                },
                {
                    "name": "ערב יוקרתי",
                    "time": "20:30 - 23:00",
                    "travel": "🚕 מונית",
                    "desc": "מתלבשים יפה ויוצאים.",
                    "spots": [
                        {"name": "Bern Restaurant", "desc": "מסעדה עם אוכל גאורגי מודרני ואווירה טובה.", "query": "Bern Restaurant Batumi"},
                        {"name": "Eclipse Casino", "desc": "למי שרוצה לנסות את המזל (בזהירות!).", "query": "Eclipse Casino Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 6,
            "title": "אופניים, דגים ופרידה",
            "desc": "יום אחרון. משלימים קניות, אוכלים טוב וטסים.",
            "areas": [
                {
                    "name": "הטיילת החדשה",
                    "time": "10:00 - 13:00",
                    "travel": "🚲 אופניים חשמליים",
                    "desc": "שוכרים אופניים ונוסעים לאורך כל הטיילת (7 ק\"מ) עד לקצה הדרומי.",
                    "spots": [
                        {"name": "נקודת תצפית למטוסים", "desc": "בסוף הטיילת, המטוסים נוחתים ממש מעל הראש.", "query": "Batumi Airport View Point"},
                        {"name": "Metro City Mall", "desc": "קניון ענק בסוף הטיילת לקניות אחרונות (מותגים).", "query": "Metro City Forum Batumi"}
                    ]
                },
                {
                    "name": "שוק הדגים (Fish Market)",
                    "time": "14:00 - 16:30",
                    "travel": "🚕 מונית",
                    "desc": "ארוחת פרידה מסורתית.",
                    "spots": [
                        {"name": "שוק הדגים", "desc": "בוחרים דגים טריים למטה.", "query": "Batumi Fish Market"},
                        {"name": "Blue Wave", "desc": "המסעדה למעלה שמכינה את הדגים שקניתם.", "query": "Blue Wave Batumi"}
                    ]
                },
                {
                    "name": "לשדה התעופה",
                    "time": "18:00",
                    "travel": "🚕 מונית",
                    "desc": "הזמנת Bolt לשדה התעופה. להגיע 3 שעות לפני!",
                    "spots": []
                }
            ]
        }
    ]
    return plan

# --- HTML & CSS ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ariel_elhayani | Batumi 2026</title>
    <style>
        :root { --blue: #0f172a; --dark: #1e293b; --bg: #f1f5f9; --white: #ffffff; --accent: #3b82f6; --green: #10b981; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; direction: rtl; background-color: var(--bg); color: var(--dark); margin: 0; padding-bottom: 60px; }

        /* Header */
        header { background: linear-gradient(135deg, #0f172a 0%, #334155 100%); color: white; padding: 40px 20px; text-align: center; border-bottom: 4px solid var(--accent); }
        h1 { margin: 0; font-size: 2.5rem; font-weight: 800; letter-spacing: 1px; }
        .subtitle { font-size: 1.2rem; opacity: 0.9; margin-top: 5px; font-weight: 400; color: #cbd5e1; }

        /* Navigation */
        .nav-wrapper { position: sticky; top: 0; z-index: 1000; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.05); padding: 12px 0; }
        .nav-container { display: flex; gap: 10px; overflow-x: auto; padding: 0 15px; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
        .nav-container::-webkit-scrollbar { display: none; }
        
        .nav-btn { flex: 0 0 auto; padding: 10px 20px; border: 1px solid #e2e8f0; background: white; color: #64748b; font-size: 1rem; font-weight: 700; border-radius: 50px; cursor: pointer; transition: all 0.2s; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }
        .nav-btn.active { background: var(--blue); color: white; border-color: var(--blue); transform: scale(1.05); box-shadow: 0 4px 15px rgba(15, 23, 42, 0.3); }
        .nav-btn.special { background: var(--accent); color: white; border: none; }
        .nav-btn.info { background: var(--green); color: white; border: none; }

        /* Layout */
        .container { max-width: 800px; margin: 25px auto; padding: 0 15px; }
        .tab-content { display: none; animation: fadeIn 0.4s ease-out; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Daily Intro */
        .day-intro { text-align: center; margin-bottom: 30px; background: white; padding: 25px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }
        .day-intro h2 { color: var(--blue); margin: 0 0 8px 0; font-size: 2rem; font-weight: 800; }
        .day-intro p { color: #64748b; margin: 0; font-size: 1.1rem; }

        /* Area Cards */
        .area-card { background: white; border-radius: 16px; padding: 25px; margin-bottom: 25px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; position: relative; overflow: hidden; }
        .area-card::before { content: ''; position: absolute; right: 0; top: 0; bottom: 0; width: 6px; background: var(--accent); }
        
        .area-header { margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px dashed #cbd5e1; }
        .area-time { display: inline-block; background: #eff6ff; color: var(--accent); padding: 5px 12px; border-radius: 8px; font-size: 0.9rem; font-weight: 800; margin-bottom: 10px; }
        .area-title { font-size: 1.6rem; font-weight: 800; color: var(--blue); margin: 0 0 5px 0; }
        .area-travel { font-size: 0.95rem; color: #f59e0b; font-weight: 600; display: flex; align-items: center; gap: 6px; margin-bottom: 8px; }
        .area-desc { font-size: 1.05rem; color: #475569; line-height: 1.6; }

        /* Spots */
        .spots-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; }
        .spot-card { background: #f8fafc; border: 1px solid #e2e8f0; padding: 18px; border-radius: 12px; display: flex; flex-direction: column; transition: transform 0.2s, border-color 0.2s; }
        .spot-card:hover { transform: translateY(-3px); border-color: var(--accent); background: white; box-shadow: 0 10px 20px rgba(0,0,0,0.05); }

        .spot-name { font-weight: 800; font-size: 1.1rem; color: var(--blue); margin-bottom: 6px; }
        .spot-desc { font-size: 0.9rem; color: #64748b; margin-bottom: 15px; flex-grow: 1; line-height: 1.5; }
        .map-link { text-decoration: none; background: white; border: 2px solid #e2e8f0; color: var(--blue); padding: 10px; border-radius: 10px; font-size: 0.9rem; font-weight: 700; text-align: center; display: block; margin-top: auto; transition: 0.2s; }
        .map-link:hover { background: var(--blue); color: white; border-color: var(--blue); }

        /* Info Pages */
        .info-page { background: white; padding: 30px; border-radius: 20px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); }
        .info-header { font-size: 1.8rem; font-weight: 800; color: var(--blue); margin-bottom: 25px; padding-bottom: 10px; border-bottom: 3px solid var(--accent); display: inline-block; }
        
        .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
        .info-box { background: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0; }
        .info-box h3 { margin: 0 0 10px 0; color: var(--blue); display: flex; align-items: center; gap: 8px; font-size: 1.2rem; }
        
        .checklist li { background: #fffbeb; border: 1px solid #fcd34d; padding: 15px; margin-bottom: 12px; border-radius: 10px; list-style: none; display: flex; gap: 15px; align-items: start; }
        .checklist strong { display: block; color: #92400e; margin-bottom: 4px; font-size: 1.05rem; }
        
        .copy-box { background: #1e293b; color: #a5f3fc; padding: 20px; border-radius: 10px; font-family: monospace; direction: ltr; text-align: left; margin-top: 15px; font-size: 0.95rem; border: 1px solid #334155; line-height: 1.6; }
        .warning-box { background: #fee2e2; color: #991b1b; padding: 15px; border-radius: 10px; border: 1px solid #fca5a5; font-weight: bold; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }

    </style>
    <script>
        function openTab(tabId, btn) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
            document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
            document.getElementById(tabId).classList.add('active');
            btn.classList.add('active');
        }
    </script>
</head>
<body>

    <header>
        <h1>ariel_elhayani</h1>
        <div class="subtitle">Batumi Trip 2026 | 6 Days Plan</div>
    </header>

    <div class="nav-wrapper">
        <div class="nav-container">
            {% for day in plan %}
            <button class="nav-btn {% if loop.first %}active{% endif %}" onclick="openTab('day{{ day.day }}', this)">
                יום {{ day.day }}
            </button>
            {% endfor %}
            <button class="nav-btn info" onclick="openTab('mustknow', this)">💡 טיפים</button>
            <button class="nav-btn special" onclick="openTab('flights', this)">✈️ טיסות</button>
            <button class="nav-btn special" onclick="openTab('airbnb', this)">🏠 דירה</button>
        </div>
    </div>

    <div class="container">

        {% for day in plan %}
        <div id="day{{ day.day }}" class="tab-content {% if loop.first %}active{% endif %}">
            <div class="day-intro">
                <h2>יום {{ day.day }}</h2>
                <p>{{ day.title }}</p>
                <div style="font-size: 1rem; color: #64748b; margin-top: 5px;">{{ day.desc }}</div>
            </div>

            {% for area in day.areas %}
            <div class="area-card">
                <div class="area-header">
                    <span class="area-time">{{ area.time }}</span>
                    <h3 class="area-title">{{ area.name }}</h3>
                    <div class="area-travel">{{ area.travel }}</div>
                    <div class="area-desc">{{ area.desc }}</div>
                </div>

                <div class="spots-container">
                    {% for spot in area.spots %}
                    <div class="spot-card">
                        <div>
                            <div class="spot-name">{{ spot.name }}</div>
                            <div class="spot-desc">{{ spot.desc }}</div>
                        </div>
                        <a href="{{ make_map_link(spot.query) }}" target="_blank" class="map-link">📍 נווט אותי</a>
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
        {% endfor %}

        <div id="mustknow" class="tab-content">
            <div class="info-page">
                <div class="info-header">🇬🇪 טיפים של אלופים</div>
                <div class="info-grid">
                    <div class="info-box">
                        <h3>💰 כסף (GEL)</h3>
                        <p>1 לארי = כ-1.4 ש"ח. תמיד תוסיפו שליש למחיר בראש. <strong>חובה מזומן</strong> לשוק ולמוניות, אשראי עובד בסופר ובמסעדות.</p>
                    </div>
                    <div class="info-box">
                        <h3>🚖 מוניות</h3>
                        <p>לא עוצרים ברחוב! מורידים <strong>Yandex Go</strong> או <strong>Bolt</strong>. נסיעה בעיר = 5-10 לארי.</p>
                    </div>
                    <div class="info-box">
                        <h3>📱 סים</h3>
                        <p>רק <strong>Magti</strong>. קונים בחנות בעיר (Batumi Mall), לא בשדה. 30 ש"ח לאינטרנט ללא הגבלה.</p>
                    </div>
                    <div class="info-box">
                        <h3>💧 מים</h3>
                        <p><strong>אסור לשתות מהברז!</strong> קונים שישיות מים מינרליים לדירה.</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="flights" class="tab-content">
            <div class="info-page">
                <div class="info-header">✈️ מדריך טיסות לקטינים</div>
                
                <div class="warning-box">
                    ⚠️ שימו לב: אתם בני 17. בלי המסמכים האלו לא יעלו אתכם לטיסה!
                </div>

                <ul class="checklist" style="padding: 0;">
                    <li>
                        <span class="check-icon">📝</span>
                        <div>
                            <strong>אישור נוטריוני (באנגלית)</strong>
                            מסמך חתום ע"י עורך דין שבו ההורים מאשרים לכם לטוס ולשהות בחו"ל לבד. זה הדבר הכי חשוב.
                        </div>
                    </li>
                    <li>
                        <span class="check-icon">🛂</span>
                        <div>
                            <strong>דרכונים בתוקף</strong>
                            לוודא שהדרכון בתוקף לפחות לחצי שנה קדימה מיום הטיסה.
                        </div>
                    </li>
                    <li>
                        <span class="check-icon">📄</span>
                        <div>
                            <strong>צילום דרכון הורים</strong>
                            שיהיה לכם בתיק צילום מודפס של הדרכונים של אבא ואמא.
                        </div>
                    </li>
                    <li>
                        <span class="check-icon">🏥</span>
                        <div>
                            <strong>ביטוח נסיעות מורחב</strong>
                            לעשות ביטוח שכולל "ספורט אתגרי" (בשביל האופנועי ים והרפטינג).
                        </div>
                    </li>
                </ul>

                <div style="margin-top: 30px;">
                    <h3 style="color: var(--blue);">🛫 נחיתה והגעה</h3>
                    <p>נוחתים בשדה התעופה הבינלאומי בטומי (BUS).<br>
                    ביציאה יקפצו עליכם נהגי מוניות - <strong>להתעלם!</strong><br>
                    מזמינים Yandex/Bolt דרך ה-Wifi של השדה. עלות: 15-20 לארי עד Orbi City.</p>
                </div>
            </div>
        </div>

        <div id="airbnb" class="tab-content">
            <div class="info-page">
                <div class="info-header">🏠 הדירה: Orbi City</div>
                <p>המלצה חמה: לקחת דירה רק בקומפלקס <strong>Orbi City</strong> (בלוק A או C). זה המקום הכי נוח ובטוח, קרוב לים ולסופר.</p>
                
                <div class="info-box" style="margin: 20px 0; border-color: var(--accent);">
                    <strong>💡 טיפ להזמנה:</strong> Airbnb לא נותן להזמין מתחת לגיל 18.
                    <br>ההורים מזמינים מהחשבון שלהם, ושולחים את ההודעה הזאת למארח <strong>לפני</strong> התשלום:
                </div>

                <div class="copy-box">
                    "Hi,<br><br>
                    I am booking this apartment for my son and his friends (3 boys, aged 17).<br>
                    They are very responsible and mature.<br>
                    I am paying for the trip, but I will not be staying with them.<br>
                    Is this okay with you?<br><br>
                    Thanks!"
                </div>
            </div>
        </div>

    </div>

</body>
</html>
"""

# הזרקת פונקציית הלינקים ל-HTML
@app.context_processor
def utility_processor():
    return dict(make_map_link=make_map_link)

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, plan=get_plan())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
