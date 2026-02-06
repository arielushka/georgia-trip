from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)


# --- פונקציית עזר ללינקים ---
def make_map_link(query):
    encoded_query = urllib.parse.quote(query)
    return f"https://www.google.com/maps/search/?api=1&query={encoded_query}"


# --- נתוני התוכנית המלאה (7 ימים) - מתוקן ומעובה ---
def get_plan():
    plan = [
        {
            "day": 1,
            "title": "נחיתה בבטומי ופתיחת שולחן",
            "desc": "מתמקמים בדירה ויוצאים ישר ללב העניינים בטיילת המפורסמת.",
            "areas": [
                {
                    "name": "Orbi City (התארגנות)",
                    "time": "16:00 - 18:00",
                    "travel": "📍 מונית משדה התעופה",
                    "desc": "צ'ק אין זריז, קניית סים (Magti) ומים בסופר למטה.",
                    "spots": [
                        {"name": "Willmart Orbi", "desc": "סופרמרקט ענק מתחת למלון להצטיידות.",
                         "query": "Willmart Orbi City"},
                        {"name": "Magti", "desc": "חנות סלולר לקניית סים מקומי (חובה).", "query": "Magti Batumi Mall"},
                        {"name": "Currency Exchange", "desc": "צ'יינג' להחלפת דולרים ללארי.",
                         "query": "Currency Exchange Batumi"}
                    ]
                },
                {
                    "name": "Batumi Boulevard (הטיילת)",
                    "time": "19:00 - 23:00",
                    "travel": "🚶 הליכה / מונית קצרה",
                    "desc": "הלב הפועם של בטומי. הליכה לאורך הים ומסעדה ראשונה.",
                    "spots": [
                        {"name": "Kiziki", "desc": "מסעדה גאורגית מעולה לחצ'אפורי וחינקלי.",
                         "query": "Kiziki Restaurant Batumi"},
                        {"name": "פסל עלי ונינו", "desc": "הפסל המפורסם שזז ומתחבר (שווה וידאו).",
                         "query": "Ali and Nino Statue"},
                        {"name": "Chacha Time", "desc": "בר מגניב לדרינק ראשון (צ'אצ'ה).",
                         "query": "Chacha Time Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 2,
            "title": "הגן הבוטני, דגים ופיאצה",
            "desc": "יום שמתחיל בטבע, ממשיך באוכל טוב ונגמר בכיכר הכי יפה בעיר.",
            "areas": [
                {
                    "name": "Mtsvane Kontskhi (הכף הירוק)",
                    "time": "10:00 - 14:00",
                    "travel": "🚖 מונית (כ-20 דק')",
                    "desc": "הגן הבוטני הענק שיושב על צוק מעל הים. נוף משוגע.",
                    "spots": [
                        {"name": "הגן הבוטני", "desc": "מסלול הליכה ירוק מול הים.", "query": "Batumi Botanical Garden"},
                        {"name": "החוף הירוק", "desc": "חוף ים צלול מתחת לגן (פחות עמוס מהעיר).",
                         "query": "Mtsvane Kontskhi Beach"}
                    ]
                },
                {
                    "name": "Argo Cable Car & דגים",
                    "time": "14:30 - 19:00",
                    "travel": "🚖 חזרה לעיר",
                    "desc": "קולינריה בשוק הדגים ותצפית מלמעלה.",
                    "spots": [
                        {"name": "Batumi Fish Market",
                         "desc": "קונים דגים טריים למטה, ומכינים לכם אותם במסעדת Blue Wave למעלה.",
                         "query": "Batumi Fish Market"},
                        {"name": "רכבל ארגו", "desc": "רכבל שעולה לתצפית על כל העיר בשקיעה.", "query": "Argo Cable Car"}
                    ]
                },
                {
                    "name": "Piazza Square (כיכר פיאצה)",
                    "time": "20:30 - אל הלילה",
                    "travel": "🚶 הליכה מהרכבל",
                    "desc": "הכיכר המרכזית. נראית כמו איטליה, מלאה בבתי קפה והופעות חיות.",
                    "spots": [
                        {"name": "La Brioche", "desc": "מקום טוב בכיכר לפיצה, קינוחים וקפה.",
                         "query": "La Brioche Piazza Batumi"},
                        {"name": "השעון המוזיקלי", "desc": "בכל שעה עגולה יוצאות דמויות מהשעון במגדל.",
                         "query": "Piazza Square Batumi"},
                        {"name": "Eclipse Casino", "desc": "למי שרוצה לסיים את הלילה בקזינו.",
                         "query": "Eclipse Casino Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 3,
            "title": "שופינג בשוק, דולפינים ומסיבות",
            "desc": "יום עמוס באטרקציות: קניות זולות, דולפינריום וחיי לילה.",
            "areas": [
                {
                    "name": "Hopa Market (שוק הופה)",
                    "time": "10:00 - 13:00",
                    "travel": "🚖 מונית",
                    "desc": "השוק הכי גדול בבטומי לבגדים, מותגים (חיקויים) ונעליים בזול.",
                    "spots": [
                        {"name": "Hopa Bazaar", "desc": "תתמקחו על המחירים! מעולה לקניית ביגוד.",
                         "query": "Hopa Market Batumi"},
                        {"name": "דוכני צ'ורצ'חלה", "desc": "יש בשוק אזור של ממתקים גאורגיים הביתה.",
                         "query": "Hopa Market Batumi Food"}
                    ]
                },
                {
                    "name": "פארק 6 במאי & דולפינריום",
                    "time": "13:30 - 16:30",
                    "travel": "🚖 מונית קצרה",
                    "desc": "האזור הקלאסי של בטומי.",
                    "spots": [
                        {"name": "Batumi Dolphinarium", "desc": "מופע דולפינים מפורסם (צריך להזמין כרטיס מראש).",
                         "query": "Batumi Dolphinarium"},
                        {"name": "אגם נורי (Nurigeli)", "desc": "בתוך הפארק, אפשר לשכור סירה ולשוט באגם.",
                         "query": "6 May Park Batumi"}
                    ]
                },
                {
                    "name": "מועדוני חוף (Beach Clubs)",
                    "time": "17:00 - 20:00",
                    "travel": "🚶 הליכה לחוף",
                    "desc": "זמן להירגע עם מוזיקה ואווירה.",
                    "spots": [
                        {"name": "Iveria Beach", "desc": "מועדון חוף יוקרתי מתחת למגדל האלפבית.",
                         "query": "Iveria Beach Batumi"},
                        {"name": "Mandarina Beach", "desc": "בר-חוף מגניב עם פופים וקוקטיילים.",
                         "query": "Mandarina Beach Bar Batumi"}
                    ]
                },
                {
                    "name": "Europe Square & Miracle Park",
                    "time": "21:00 - הלילה",
                    "travel": "🚶 הליכה בטיילת",
                    "desc": "מרכז העניינים בלילה.",
                    "spots": [
                        {"name": "Europe Square", "desc": "פסל מדיאה (זאת שמחזיקה גיזת זהב).",
                         "query": "Europe Square Batumi"},
                        {"name": "Miracle Park", "desc": "איזור הגלגל הענק ומגדל האלפבית המואר.",
                         "query": "Miracle Park Batumi"},
                        {"name": "Soho / Sector 26", "desc": "המועדונים הכי חזקים ללילה.", "query": "Sector 26 Batumi"}
                    ]
                }
            ]
        },
        {
            "day": 4,
            "title": "הרים ומפלים (יוצאים מהעיר)",
            "desc": "טיול ג'יפים/נהג פרטי לטבע של מחוז אג'ריה.",
            "areas": [
                {
                    "name": "שמורת מחונצטי (Makhuntseti)",
                    "time": "10:00 - 15:00",
                    "travel": "🚖 נהג צמוד ליום",
                    "desc": "כ-50 דקות נסיעה מבטומי. טבע נטו.",
                    "spots": [
                        {"name": "מפל מחונצטי", "desc": "המפל הגדול והמפורסם.", "query": "Makhuntseti Waterfall"},
                        {"name": "גשר המלכה תמר", "desc": "גשר אבן עתיק מעל הנהר (טוב לתמונות).",
                         "query": "Queen Tamar Bridge"},
                        {"name": "רפטינג", "desc": "יש נקודות בנהר בדרך שאפשר לעשות רפטינג קליל.",
                         "query": "Rafting Makhuntseti"}
                    ]
                },
                {
                    "name": "Adjarian Wine House",
                    "time": "15:30 - 17:30",
                    "travel": "🚙 בדרך חזרה",
                    "desc": "ארוחת צהריים מאוחרת במקום הכי יפה באזור.",
                    "spots": [
                        {"name": "בית היין האג'רי", "desc": "מסעדה בתוך יקב עתיק, אוכל מעולה ונוף.",
                         "query": "Adjarian Wine House"}
                    ]
                },
                {
                    "name": "נסיעה לטביליסי",
                    "time": "18:30 - 23:30",
                    "travel": "🚅 רכבת מהירה / נהג",
                    "desc": "עוזבים את בטומי ועוברים לעיר הבירה.",
                    "spots": [
                        {"name": "Batumi Central Station", "desc": "תחנת הרכבת.", "query": "Batumi Central Station"},
                        {"name": "דירה בטביליסי", "desc": "הגעה והתמקמות.", "query": "Tbilisi Center"}
                    ]
                }
            ]
        },
        {
            "day": 5,
            "title": "טביליסי: שווקים, עתיקות וספא",
            "desc": "היום הראשון בבירה - שילוב של היסטוריה והיפסטרים.",
            "areas": [
                {
                    "name": "Dry Bridge Market (שוק הפשפשים)",
                    "time": "10:00 - 13:00",
                    "travel": "🚖 מונית",
                    "desc": "שוק ענק מתחת לגשר. עתיקות, מצלמות, תקליטים ותכשיטים.",
                    "spots": [
                        {"name": "הגשר היבש", "desc": "השוק עצמו. חובה להתמקח.", "query": "Dry Bridge Market Tbilisi"},
                        {"name": "Dedaena Park", "desc": "פארק סקייטרים צמוד, מקום מגניב להסתובב.",
                         "query": "Dedaena Park"}
                    ]
                },
                {
                    "name": "Fabrika (המתחם ההיפסטרי)",
                    "time": "13:30 - 15:30",
                    "travel": "🚖 מונית קצרה",
                    "desc": "מפעל תפירה שהפך להוסטל ומרכז בילוי. קירות גרפיטי ומסעדות.",
                    "spots": [
                        {"name": "חצר פבריקה", "desc": "מלא מסעדות (המבורגר, ראמן, גאורגי) באווירה צעירה.",
                         "query": "Fabrika Tbilisi"}
                    ]
                },
                {
                    "name": "Abanotubani (בתי המרחץ)",
                    "time": "16:30 - 19:00",
                    "travel": "🚖 מונית לעיר העתיקה",
                    "desc": "רובע בתי המרחץ המפורסם (גופרית).",
                    "spots": [
                        {"name": "Gulo's Spa / Chreli Abano",
                         "desc": "חובה להזמין חדר פרטי ולבקש מסאז' 'קיסה' (קרצוף).", "query": "Gulo's Spa Tbilisi"},
                        {"name": "מפל הבוטניקל", "desc": "מפל נסתר ממש בתוך העיר העתיקה (בסוף הרחוב).",
                         "query": "Leghvtakhevi Waterfall"}
                    ]
                },
                {
                    "name": "Shardeni Street (חיי לילה)",
                    "time": "21:00 - הלילה",
                    "travel": "🚶 הליכה",
                    "desc": "מדרחוב מלא בברים, נרגילות ומועדונים.",
                    "spots": [
                        {"name": "Shardeni St", "desc": "פשוט ללכת ולבחור איפה לשבת.",
                         "query": "Shardeni Street Tbilisi"}
                    ]
                }
            ]
        },
        {
            "day": 6,
            "title": "הקווקז הגבוה: קזבגי (Stepantsminda)",
            "desc": "היום עם הנוף הכי יפה בטיול. חובה לקחת נהג ליום שלם.",
            "areas": [
                {
                    "name": "הדרך הצבאית",
                    "time": "09:00 - 12:00",
                    "travel": "🚙 נסיעה צפונה",
                    "desc": "הדרך עצמה היא אטרקציה. עוצרים לצילומים.",
                    "spots": [
                        {"name": "Zhinvali Reservoir", "desc": "אגם טורקיז ענק.", "query": "Zhinvali Reservoir"},
                        {"name": "Ananuri Fortress", "desc": "מבצר עתיק על שפת האגם.", "query": "Ananuri Fortress"},
                        {"name": "אנדרטת הידידות", "desc": "מרפסת תצפית עגולה על צוק.",
                         "query": "Russia–Georgia Friendship Monument"}
                    ]
                },
                {
                    "name": "Gergeti Trinity Church",
                    "time": "13:00 - 15:00",
                    "travel": "🚙 ג'יפים להר",
                    "desc": "הכנסייה המפורסמת מול הר הקזבק המושלג.",
                    "spots": [
                        {"name": "כנסיית השילוש", "desc": "הנקודה הכי יפה בגאורגיה.", "query": "Gergeti Trinity Church"}
                    ]
                },
                {
                    "name": "Rooms Hotel",
                    "time": "15:30 - 17:00",
                    "travel": "🚙 ירידה לעיירה",
                    "desc": "ארוחת צהריים/קפה במרפסת של המלון הכי מפורסם.",
                    "spots": [
                        {"name": "Rooms Hotel Kazbegi", "desc": "המרפסת פתוחה גם למי שלא ישן במלון. נוף משוגע.",
                         "query": "Rooms Hotel Kazbegi"}
                    ]
                }
            ]
        },
        {
            "day": 7,
            "title": "שופינג ולונה פארק על ההר",
            "desc": "קונים מתנות, עולים ללונה פארק וטסים הביתה.",
            "areas": [
                {
                    "name": "קניונים ושופינג",
                    "time": "10:00 - 14:00",
                    "travel": "🚖 מונית",
                    "desc": "מותגים בזול לפני הטיסה.",
                    "spots": [
                        {"name": "Galleria Tbilisi", "desc": "קניון ממש בכיכר החירות (מרכז העיר).",
                         "query": "Galleria Tbilisi"},
                        {"name": "East Point", "desc": "קניון ענק פתוח ביציאה מהעיר (קרוב לשדה).",
                         "query": "East Point Tbilisi"}
                    ]
                },
                {
                    "name": "Mtatsminda Park (הפארק על ההר)",
                    "time": "15:00 - 19:00",
                    "travel": "🚋 פוניקולר (רכבת שיניים)",
                    "desc": "פארק שעשועים שמשקיף על כל טביליסי מלמעלה.",
                    "spots": [
                        {"name": "Tbilisi Funicular", "desc": "הרכבת שעולה למעלה (חוויה בפני עצמה).",
                         "query": "Tbilisi Funicular"},
                        {"name": "גלגל ענק", "desc": "רואים ממנו את כל העיר.", "query": "Mtatsminda Park Ferris Wheel"},
                        {"name": "מסעדת הפוניקולר", "desc": "ארוחת סיום חגיגית מול הנוף.",
                         "query": "Funicular Restaurant Complex"}
                    ]
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
    <title>ariel_elhayani | Georgia 2026</title>
    <style>
        :root { --blue: #2c3e50; --dark: #1a252f; --bg: #f3f4f6; --white: #ffffff; --accent: #e74c3c; --green: #10b981; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; direction: rtl; background-color: var(--bg); color: var(--dark); margin: 0; padding-bottom: 60px; }

        /* Header */
        header { background: linear-gradient(135deg, #1e293b, #334155); color: white; padding: 30px 20px; text-align: center; border-bottom: 5px solid var(--accent); }
        h1 { margin: 0; font-size: 2.2rem; font-weight: 800; letter-spacing: 1px; }
        .subtitle { font-size: 1.1rem; opacity: 0.8; margin-top: 5px; font-weight: 400; }

        /* Nav */
        .nav-wrapper { position: sticky; top: 0; z-index: 1000; background: rgba(255,255,255,0.95); backdrop-filter: blur(5px); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); padding: 10px 0; }
        .nav-container { display: flex; gap: 10px; overflow-x: auto; padding: 0 15px; -webkit-overflow-scrolling: touch; scrollbar-width: none; }
        .nav-container::-webkit-scrollbar { display: none; }

        .nav-btn { flex: 0 0 auto; padding: 8px 16px; border: 1px solid #e2e8f0; background: white; color: #64748b; font-size: 0.95rem; font-weight: 700; border-radius: 50px; cursor: pointer; transition: all 0.2s; }
        .nav-btn.active { background: var(--blue); color: white; border-color: var(--blue); transform: scale(1.05); box-shadow: 0 4px 12px rgba(44, 62, 80, 0.2); }
        .nav-btn.special { background: var(--accent); color: white; border: none; }
        .nav-btn.info { background: var(--green); color: white; border: none; }

        /* Layout */
        .container { max-width: 800px; margin: 20px auto; padding: 0 15px; }

        .tab-content { display: none; animation: fadeIn 0.4s ease-out; }
        .tab-content.active { display: block; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }

        /* Section Title */
        .day-intro { text-align: center; margin-bottom: 25px; background: white; padding: 20px; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        .day-intro h2 { color: var(--blue); margin: 0 0 5px 0; font-size: 1.8rem; }
        .day-intro p { color: #64748b; margin: 0; font-size: 1.05rem; }

        /* Area Cards */
        .area-card { background: white; border-radius: 16px; padding: 20px; margin-bottom: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); position: relative; border-right: 5px solid var(--accent); }

        .area-header { margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px dashed #e2e8f0; }
        .area-time { display: inline-block; background: #eff6ff; color: #2563eb; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; font-weight: 800; margin-bottom: 8px; }
        .area-title { font-size: 1.5rem; font-weight: 800; color: var(--blue); margin: 0 0 5px 0; line-height: 1.2; }
        .area-travel { font-size: 0.9rem; color: #f59e0b; font-weight: 600; display: flex; align-items: center; gap: 6px; margin-bottom: 8px; }
        .area-desc { font-size: 1rem; color: #475569; line-height: 1.5; }

        /* Grid Spots */
        .spots-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 12px; }
        .spot-card { background: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 10px; display: flex; flex-direction: column; justify-content: space-between; transition: transform 0.2s; }
        .spot-card:hover { transform: translateY(-3px); border-color: var(--blue); background: white; }

        .spot-name { font-weight: 700; font-size: 1rem; color: var(--dark); margin-bottom: 4px; }
        .spot-desc { font-size: 0.85rem; color: #64748b; margin-bottom: 12px; flex-grow: 1; line-height: 1.4; }

        .map-link { text-decoration: none; background: white; border: 1px solid #cbd5e1; color: var(--blue); padding: 8px; border-radius: 8px; font-size: 0.85rem; font-weight: 700; text-align: center; display: block; margin-top: auto; }
        .map-link:hover { background: var(--blue); color: white; border-color: var(--blue); }

        /* Info & Checklist Styles */
        .info-page { background: white; padding: 25px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .info-header { font-size: 1.6rem; font-weight: 800; color: var(--blue); margin-bottom: 20px; border-bottom: 3px solid var(--accent); display: inline-block; padding-bottom: 5px; }

        .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
        .info-box { background: #f8fafc; padding: 15px; border-radius: 10px; border: 1px solid #e2e8f0; }
        .info-box h3 { margin: 0 0 10px 0; font-size: 1.1rem; color: var(--dark); display: flex; align-items: center; gap: 8px; }
        .info-box p { margin: 0; font-size: 0.95rem; color: #475569; line-height: 1.5; }

        .checklist li { background: #fffbeb; border: 1px solid #fcd34d; padding: 12px; margin-bottom: 10px; border-radius: 8px; list-style: none; display: flex; gap: 12px; align-items: start; }
        .check-icon { font-size: 1.2rem; }

        .copy-box { background: #1e293b; color: #a5f3fc; padding: 15px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; margin-top: 15px; font-size: 0.9rem; border: 1px solid #334155; }

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
        <div class="subtitle">Georgia Trip 2026 | The Final Plan</div>
    </header>

    <div class="nav-wrapper">
        <div class="nav-container">
            {% for day in plan %}
            <button class="nav-btn {% if loop.first %}active{% endif %}" onclick="openTab('day{{ day.day }}', this)">
                יום {{ day.day }}
            </button>
            {% endfor %}
            <button class="nav-btn info" onclick="openTab('mustknow', this)">💡 גאורגיה</button>
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
                <div style="font-size: 0.9rem; color: #94a3b8; margin-top: 5px;">{{ day.desc }}</div>
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
                <div class="info-header">🇬🇪 דברים שחייב לדעת על גאורגיה</div>
                <div class="info-grid">
                    <div class="info-box">
                        <h3>💰 כסף (לארי - GEL)</h3>
                        <p>1 לארי = כ-1.4 ש"ח. החישוב בראש: תוסיפו שליש למחיר. <strong>חובה מזומן</strong> בשווקים ובמוניות לפעמים, אשראי עובד בסופר ובמסעדות גדולות.</p>
                    </div>
                    <div class="info-box">
                        <h3>🚖 מוניות (Yandex/Bolt)</h3>
                        <p>בחיים לא לעצור מונית ברחוב! תמיד יעקצו תיירים. תורידו <strong>Yandex Go</strong> או <strong>Bolt</strong>. נסיעה בעיר עולה גרושים (5-10 לארי).</p>
                    </div>
                    <div class="info-box">
                        <h3>📱 סים ואינטרנט</h3>
                        <p>החברה הכי טובה היא <strong>Magti</strong>. אל תקנו בשדה התעופה (יקר). לכו לחנות בעיר, סים עם אינטרנט ללא הגבלה לשבוע עולה כ-30 ש"ח.</p>
                    </div>
                    <div class="info-box">
                        <h3>💧 מים</h3>
                        <p><strong>אסור לשתות מהברז!</strong> המים לא טובים לשתייה. תקנו שישיות מים מינרליים לדירה מהסופר.</p>
                    </div>
                    <div class="info-box">
                        <h3>🍽️ טיפים במסעדות</h3>
                        <p>ברוב המקומות מוסיפים אוטומטית 10-15% "Service Charge" לחשבון. תבדקו לפני שאתם משאירים עוד טיפ.</p>
                    </div>
                    <div class="info-box">
                        <h3>🐶 כלבים ברחוב</h3>
                        <p>יש המון כלבים משוטטים. אלה שיש להם תג על האוזן מחוסנים וידידותיים, אבל עדיף לא ללטף סתם.</p>
                    </div>
                </div>
            </div>
        </div>

        <div id="flights" class="tab-content">
            <div class="info-page">
                <div class="info-header">✈️ צ'ק ליסט טיסות (נוער)</div>
                <ul class="checklist" style="padding: 0;">
                    <li>
                        <span class="check-icon">📝</span>
                        <div><strong>אישור נוטריוני:</strong> חובה! מסמך חתום ע"י עו"ד (באנגלית) שההורים מאשרים לכם לטוס לבד.</div>
                    </li>
                    <li>
                        <span class="check-icon">🛂</span>
                        <div><strong>דרכונים:</strong> לוודא תוקף לחצי שנה קדימה. שימו בתיק גם צילום דרכונים של ההורים.</div>
                    </li>
                    <li>
                        <span class="check-icon">🏥</span>
                        <div><strong>ביטוח:</strong> חובה ביטוח עם הרחבת "ספורט אתגרי" (לאופנועי ים/טרקטורונים).</div>
                    </li>
                </ul>
            </div>
        </div>

        <div id="airbnb" class="tab-content">
            <div class="info-page">
                <div class="info-header">🏠 הזמנת דירה (טיפ זהב)</div>
                <p>Airbnb בעייתיים עם גיל 18. הנה איך עוקפים את זה:</p>
                <div style="background: #e0f2fe; padding: 15px; border-radius: 8px; color: #0369a1; font-weight: bold; margin-bottom: 15px;">
                    ההורים מזמינים מהחשבון שלהם, אבל שולחים הודעה למארח *לפני* התשלום.
                </div>
                <p>הודעה למארח (תעתיקו):</p>
                <div class="copy-box">
                    "Hi,<br>
                    I am booking for my son and his friends (3 boys, aged 17).<br>
                    They are responsible. I am paying, but won't stay with them.<br>
                    We prefer Orbi City complex.<br>
                    Is this okay?"
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