from flask import Flask, render_template_string

app = Flask(__name__)

# --- תבנית ה-HTML וה-CSS ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyber Roadmap - המסלול המלא</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@300;400;600;800&display=swap" rel="stylesheet">
    
    <style>
        :root {
            --bg-dark: #0f172a;
            --card-bg: #1e293b;
            --card-hover: #2d3748;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --accent: #0ea5e9;
            --accent-glow: rgba(14, 165, 233, 0.3);
        }

        body {
            background-color: var(--bg-dark);
            color: var(--text-main);
            font-family: 'Rubik', sans-serif;
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero-section {
            padding: 80px 0;
            text-align: center;
            background: radial-gradient(circle at center, #1e293b 0%, #0f172a 70%);
            border-bottom: 1px solid #334155;
            margin-bottom: 50px;
        }

        .hero-title {
            font-weight: 800;
            background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px;
        }

        /* Course Cards */
        .course-card {
            background: var(--card-bg);
            border: 1px solid #334155;
            border-radius: 16px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            overflow: hidden;
        }

        .course-card:hover {
            border-color: var(--accent);
            box-shadow: 0 0 20px var(--accent-glow);
            background: var(--card-hover);
        }

        .card-header-content {
            padding: 25px;
            display: flex;
            align-items: center;
            position: relative;
        }

        .icon-box {
            width: 60px;
            height: 60px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            background: rgba(255,255,255,0.05);
            margin-left: 20px;
            flex-shrink: 0;
        }

        .expand-icon {
            margin-right: auto;
            color: var(--text-muted);
            transition: transform 0.3s;
        }

        .course-card[aria-expanded="true"] .expand-icon {
            transform: rotate(180deg);
            color: var(--accent);
        }

        /* Expanded Details Section */
        .course-details {
            background: rgba(0,0,0,0.2);
            border-top: 1px solid #334155;
            padding: 0; /* Animated height needs padding 0 initially if using pure css, but bootstrap handles it */
        }

        .details-inner {
            padding: 30px;
        }

        .section-title {
            color: var(--accent);
            font-weight: 700;
            font-size: 1.1rem;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        
        .section-title i { margin-left: 10px; }

        .syllabus-list li {
            margin-bottom: 8px;
            color: var(--text-muted);
        }
        
        .syllabus-list li::marker {
            color: var(--accent);
        }

        /* Practice Box inside Details */
        .practice-box {
            background: linear-gradient(145deg, #2d1b2d, #1a101a);
            border: 1px solid #ef4444;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
        }

        .btn-action {
            padding: 10px 25px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            display: inline-block;
            transition: 0.3s;
        }

        .btn-cisco {
            background: transparent;
            border: 2px solid var(--accent);
            color: var(--accent);
        }
        .btn-cisco:hover { background: var(--accent); color: white; }

        .btn-hack {
            background: #ef4444;
            color: white;
            border: none;
        }
        .btn-hack:hover { background: #dc2626; box-shadow: 0 0 15px rgba(239, 68, 68, 0.4); color: white;}

        /* Video Container */
        .video-container {
            position: relative;
            padding-bottom: 56.25%; /* 16:9 */
            height: 0;
            border-radius: 12px;
            overflow: hidden;
            margin-top: 20px;
            border: 1px solid #334155;
        }
        
        .video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

    </style>
</head>
<body>

    <div class="hero-section">
        <div class="container">
            <h1 class="display-3 hero-title">CYBER ROADMAP</h1>
            <p class="lead text-muted">לחץ על כל שלב כדי לראות את הפירוט המלא, חומרי הלימוד והתרגול</p>
        </div>
    </div>

    <div class="container pb-5">
        <div class="row justify-content-center">
            <div class="col-lg-9">
                
                {% for course in courses %}
                <div class="course-card" data-bs-toggle="collapse" data-bs-target="#collapse{{ course.id }}" aria-expanded="false">
                    <div class="card-header-content">
                        <span class="h1 fw-bold text-white-50 ms-3 mb-0">{{ course.id }}</span>
                        
                        <div class="icon-box" style="color: {{ course.color }}; border: 1px solid {{ course.color }}">
                            <i class="fas {{ course.icon }}"></i>
                        </div>
                        
                        <div class="flex-grow-1">
                            <h4 class="mb-1 fw-bold text-white">{{ course.title }}</h4>
                            <span class="badge bg-dark border border-secondary">
                                <i class="far fa-clock ms-1"></i> {{ course.duration }}
                            </span>
                        </div>
                        
                        <div class="expand-icon">
                            <i class="fas fa-chevron-down fa-lg"></i>
                        </div>
                    </div>

                    <div class="collapse" id="collapse{{ course.id }}">
                        <div class="course-details">
                            <div class="details-inner">
                                
                                <div class="row">
                                    <div class="col-md-7">
                                        <div class="mb-4">
                                            <div class="section-title"><i class="fas fa-info-circle"></i> על הקורס</div>
                                            <p class="text-muted">{{ course.long_description }}</p>
                                        </div>

                                        <div class="mb-4">
                                            <div class="section-title"><i class="fas fa-list-ul"></i> מה לומדים?</div>
                                            <ul class="syllabus-list ps-3">
                                                {% for topic in course.syllabus %}
                                                <li>{{ topic }}</li>
                                                {% endfor %}
                                            </ul>
                                        </div>

                                        <a href="https://www.netacad.com/catalogs/learn" target="_blank" class="btn btn-action btn-cisco mt-2">
                                            מעבר לקורס באתר סיסקו <i class="fas fa-external-link-alt ms-2"></i>
                                        </a>
                                    </div>

                                    <div class="col-md-5">
                                        {% if course.practice_link %}
                                        <div class="practice-box">
                                            <h5 class="text-danger fw-bold mb-3"><i class="fas fa-biohazard ms-2"></i> זמן תרגול!</h5>
                                            <p class="small text-white-50">{{ course.practice_text }}</p>
                                            
                                            {% if course.youtube_id %}
                                            <div class="mb-3">
                                                <small class="text-white d-block mb-2">פלייליסט פתרונות והסברים:</small>
                                                <div class="video-container" style="padding-bottom: 50%;">
                                                    <iframe src="https://www.youtube.com/embed/{{ course.youtube_id }}" frameborder="0" allowfullscreen></iframe>
                                                </div>
                                            </div>
                                            {% endif %}

                                            <a href="{{ course.practice_link }}" target="_blank" class="btn btn-action btn-hack w-100">
                                                התחל לתרגל <i class="fas fa-arrow-left ms-2"></i>
                                            </a>
                                        </div>
                                        {% else %}
                                        <div class="h-100 d-flex align-items-center justify-content-center text-muted opacity-25">
                                            <i class="fas {{ course.icon }} fa-8x"></i>
                                        </div>
                                        {% endif %}
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
                {% endfor %}

            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

# --- הנתונים (התוכן העשיר) ---
courses_data = [
    {
        "id": 1, 
        "title": "Networking Basics", 
        "duration": "25 שעות", 
        "color": "#38bdf8", 
        "icon": "fa-wifi",
        "long_description": "זהו השער לעולם התקשורת. כאן לא רק לומדים 'איך לחבר כבל', אלא מבינים את השפה שבה מחשבים מדברים. נלמד איך המידע מתפרק לחבילות קטנות, איך הוא מוצא את הדרך לצד השני, ומה קורה כשהוא הולך לאיבוד.",
        "syllabus": [
            "ההבדל בין LAN ל-WAN",
            "כתובות IP ו-MAC Addresses",
            "תקשורת P2P מול Client-Server",
            "רכיבי רשת: ראוטר, סוויץ' ומודם"
        ],
        "practice_link": "",
        "practice_text": ""
    },
    {
        "id": 2, 
        "title": "Packet Tracer", 
        "duration": "10 שעות", 
        "color": "#818cf8", 
        "icon": "fa-laptop-code",
        "long_description": "לפני שנוגעים בציוד אמיתי (ויקר), לומדים לעבוד על הסימולטור. Packet Tracer היא תוכנה המאפשרת לגרור ראוטרים למסך, לחבר כבלים וירטואליים ולראות את המידע זורם בזמן אמת. זהו כלי חובה לכל איש סייבר.",
        "syllabus": [
            "התקנת התוכנה והכרת הממשק",
            "בניית רשת ביתית פשוטה",
            "הגדרת כתובות IP במחשבים וירטואליים",
            "סימולציה של שליחת הודעות (Ping)"
        ],
        "practice_link": "",
        "practice_text": ""
    },
    {
        "id": 3, 
        "title": "Networking Essentials", 
        "duration": "70 שעות", 
        "color": "#c084fc", 
        "icon": "fa-network-wired",
        "long_description": "הקורס הזה הוא הליבה של הידע שלך. אם תדע אותו טוב, תהיה לך עליונות על פני האקרים מתחילים. כאן נכנסים לעומק של הפרוטוקולים שמניעים את האינטרנט ומבינים איפה קבורות חולשות האבטחה.",
        "syllabus": [
            "מודל ה-OSI (שבע השכבות) - קריטי!",
            "פרוטוקולי TCP ו-UDP",
            "ניתוב (Routing) ו-Subnetting",
            "שירותי רשת: DHCP, DNS, NAT"
        ],
        # כאן אנחנו משלבים את התרגול!
        "practice_link": "https://tryhackme.com/path/outline/presecurity",
        "practice_text": "זה הזמן לעצור את התיאוריה ולעבור למעשים! כנס למסלול Pre-Security ב-TryHackMe. הוא חופף לחומר של הקורס הזה ומאפשר לך לראות את הדברים 'בעיניים של האקר'.",
        "youtube_id": "videoseries?list=PLBf0hzazHTGMuTpqpdxbDjwSEn7w_S0-d" # פלייליסט של TryHackMe Pre-Security
    },
    {
        "id": 4, 
        "title": "Intro to Cybersecurity", 
        "duration": "15 שעות", 
        "color": "#f472b6", 
        "icon": "fa-shield-alt",
        "long_description": "עכשיו כשיש לך בסיס ברשתות, אפשר להתחיל לדבר על הגנה ותקיפה. הקורס הזה נותן סקירה רחבה על עולם הסייבר: מי הם התוקפים? מה הם רוצים? ואיך ארגונים מתגוננים?",
        "syllabus": [
            "סוגי תוקפים (כובע לבן/שחור)",
            "נוזקות (Malware): וירוסים, כופרה וסוסים טרויאנים",
            "הנדסה חברתית (Social Engineering)",
            "עקרונות ה-CIA (Sodiyut, Shlemut, Zminut)"
        ],
        "practice_link": "https://tryhackme.com/room/introtooffensivesecurity",
        "practice_text": "מומלץ לבצע את החדר 'Intro to Offensive Security' כדי להרגיש איך זה להיות בצד התוקף.",
        "youtube_id": "fNZdXq2jXWU" # סרטון מבוא לסייבר
    },
    {
        "id": 5, 
        "title": "Linux Unhatched", 
        "duration": "8 שעות", 
        "color": "#fbbf24", 
        "icon": "fa-terminal",
        "long_description": "מערכת ההפעלה של ההאקרים. אין כלי פריצה רציני שיש לו ממשק גרפי יפה - הכל קורה בשורת הפקודה. הקורס הזה יוריד לך את הפחד מהמסך השחור.",
        "syllabus": [
            "למה לינוקס משמשת בסייבר?",
            "ניווט בתיקיות דרך ה-Terminal",
            "הרשאות קבצים (Permissions)",
            "פקודות בסיסיות שחובה להכיר"
        ],
        "practice_link": "https://tryhackme.com/module/linux-fundamentals",
        "practice_text": "במקביל לקורס, חובה לתרגל את Linux Fundamentals. שם תכתוב את הפקודות בעצמך בתוך מכונה וירטואלית.",
        "youtube_id": "lZAoFs75_cs" # סרטון לינוקס
    }
]

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, courses=courses_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
