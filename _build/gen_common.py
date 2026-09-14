"""InKozi static page generator — shared data, helpers and page shell.
Run:  python3 _build/gen_all.py   (from the repo root)"""
import html as H, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'
OUT = ROOT + 'admin/'

NAV = [
  ("Overview", [("index.html","bi-grid-1x2-fill","Dashboard",None),("reports.html","bi-bar-chart-line-fill","Reports",None),("notifications.html","bi-bell-fill","Notifications","6")]),
  ("Marketplace", [("users.html","bi-people-fill","Users",None),("providers.html","bi-briefcase-fill","Providers",None),("verifications.html","bi-patch-check-fill","Verifications","9 hot"),("territories.html","bi-pin-map-fill","Territories",None),("inquiries.html","bi-send-fill","Inquiries",None),("affiliates.html","bi-shop","Affiliates","3"),("connections.html","bi-diagram-3-fill","Partner connections",None)]),
  ("Community", [("questions.html","bi-chat-square-text-fill","Q&A questions","7"),("default-questions.html","bi-list-check","Default questions",None),("reviews.html","bi-star-fill","Reviews","3"),("live-chat.html","bi-chat-dots-fill","Live chat",None),("kozi-intake.html","bi-robot","Kozi AI intake",None)]),
  ("Revenue", [("payments.html","bi-credit-card-2-front-fill","Payments & invoices",None),("subscriptions.html","bi-arrow-repeat","Hosting & pricing",None),("agreements.html","bi-pen-fill","Agreements & e-sign","2")]),
  ("Marketing", [("advertisements.html","bi-badge-ad-fill","Advertisements",None),("coupons.html","bi-ticket-perforated-fill","Coupons & promo codes",None),("newsletters.html","bi-envelope-paper-fill","Newsletters",None),("press-releases.html","bi-newspaper","Press releases",None)]),
  ("Content", [("homepage.html","bi-house-heart-fill","Homepage",None),("pages.html","bi-file-earmark-text-fill","Site pages",None),("blog.html","bi-journal-richtext","Blog",None),("faq.html","bi-question-circle-fill","FAQ",None),("practice-areas.html","bi-tags-fill","Practice areas",None),("locations.html","bi-geo-alt-fill","Locations",None),("resources.html","bi-book-fill","Resources",None),("testimonials.html","bi-chat-quote-fill","Testimonials",None),("leadership.html","bi-person-badge-fill","Leadership team",None),("legal.html","bi-shield-fill-check","Legal pages",None)]),
  ("Support", [("support.html","bi-inbox-fill","Support inbox","5 hot"),("demo-requests.html","bi-calendar2-check-fill","Demo & sales",None)]),
  ("System", [("team.html","bi-shield-lock-fill","Staff & roles",None),("mobile-app.html","bi-phone-fill","Ask KOZI app",None),("audit-log.html","bi-clock-history","Audit log",None),("settings.html","bi-gear-fill","Settings",None)]),
]

# name: (img, headline, city, state, rating, reviews, phone, status, answers, email)
PROV = {
  "Amir A. Ladan":     ("assets/images/lawyer-1.jpg","Criminal Defense • DUI / DWI","Orlando","FL",4.9,128,"(407) 555-0123","Verified",312,"amir@ladanlaw.com"),
  "Sarah J. Connor":   ("assets/images/lawyer-2.jpg","Family Law • Divorce","Miami","FL",5.0,84,"(305) 555-0142","Verified",204,"sarah@connorfamilylaw.com"),
  "Maria E. Gonzalez": ("assets/images/lawyer-3.jpg","Criminal Defense • Immigration • Personal Injury","Tampa","FL",4.7,72,"(407) 555-0144","Verified",187,"maria@gonzalezlegal.com"),
  "Michael T. Ross":   (None,"Corporate Law • M&A","Tampa","FL",4.8,112,"(813) 555-0170","Verified",58,"mross@rosscorporate.com"),
  "Jessica Pearson":   (None,"Real Estate • Tax Law","Jacksonville","FL",4.9,95,"(904) 555-0119","Verified",41,"jessica@pearsonrealty.law"),
  "John P. Morgan":    (None,"DUI Defense","Orlando","FL",4.8,96,"(407) 555-0188","Verified",133,"john@morgandui.com"),
  "David Kim":         (None,"Bankruptcy","Los Angeles","CA",4.6,51,"(213) 555-0161","Verified",77,"david@kimbankruptcy.com"),
  "Harvey Specter":    (None,"Personal Injury","Miami","FL",4.8,63,"(305) 555-0190","Verified",29,"harvey@specterinjury.com"),
  "Elena Rodriguez":   (None,"Immigration","Austin","TX",4.9,38,"(512) 555-0133","Pending",0,"elena@rodriguezimmigration.com"),
  "Rachel Kim":        (None,"DUI / DWI","Tampa","FL",0,0,"(813) 555-0210","Pending",0,"rachel@kimdefense.com"),
  "Omar Haddad":       (None,"Bail Bonds","Fort Lauderdale","FL",3.7,22,"(954) 555-0098","Past due",4,"omar@haddadbail.com"),
  "Laura Chen":        (None,"Chiropractic","Orlando","FL",4.6,61,"(407) 555-0177","Verified",0,"laura@chenchiro.com"),
  "Daniel Whitaker":   (None,"DUI / DWI • Traffic Violations","Orlando","FL",4.5,34,"(407) 555-0152","Verified",22,"daniel@whitakerlaw.com"),
}

# name: (city, state, phone, status, questions, joined, last active)
USERS = {
  "Jasmine Rivera":  ("Orlando","FL","(407) ••• 0123","Active",2,"12 Mar 2026","2 min ago"),
  "Michael Turner":  ("Orlando","FL","(407) ••• 8841","Active",1,"3 Feb 2026","1 hr ago"),
  "David Lopez":     ("Orlando","FL","(407) ••• 2210","Active",1,"19 Jan 2026","Yesterday"),
  "Tom Becker":      ("Orlando","FL","(407) ••• 7734","Active",1,"14 Sep 2026","2 hrs ago"),
  "Aisha Khan":      ("Miami","FL","(305) ••• 5519","Active",1,"2 Aug 2026","5 hrs ago"),
  "Carlos Mendez":   ("Tampa","FL","(813) ••• 0098","Active",1,"14 Sep 2026","40 min ago"),
  "Priya Natarajan": ("Austin","TX","(512) ••• 6402","Active",1,"13 Sep 2026","Yesterday"),
  "Kevin O'Neil":    ("Los Angeles","CA","(213) ••• 1187","Active",1,"11 Sep 2026","2 days ago"),
  "Lucas Nguyen":    ("Orlando","FL","(407) ••• 9930","Active",1,"6 Jul 2026","3 days ago"),
  "Hannah Reed":     ("Tampa","FL","(813) ••• 4470","Unverified",1,"14 Sep 2026","2 hrs ago"),
  "Sofia Martins":   ("Fort Lauderdale","FL","(954) ••• 2231","Inactive",1,"22 May 2026","1 month ago"),
  "Victor Alves":    ("Miami","FL","(305) ••• 8890","Suspended",0,"1 Sep 2026","1 week ago"),
}

AREAS = ["Criminal Defense","DUI / DWI","Family Law","Personal Injury","Immigration","Bankruptcy","Real Estate","Employment","Corporate Law","Tax Law","Traffic Violations","Drug Crimes","Expungements","Divorce","Estate Planning","Business Law","Medical Malpractice","Workers' Compensation","Landlord-Tenant","Consumer Protection","Civil Rights","Intellectual Property","Social Security Disability","Elder Law","Insurance Claims","Bail Bonds","Chiropractic","Child Custody"]
HOME_TILES = ["Criminal Defense","DUI / Traffic","Family Law","Personal Injury","Immigration","Bankruptcy","More Areas"]
CITIES = [("Miami","FL",522),("Tampa","FL",412),("Jacksonville","FL",398),("Fort Lauderdale","FL",312),("Orlando","FL",152),("Austin","TX",64),("Los Angeles","CA",118),("New York","NY",96)]
STATES = ["Florida","Texas","California","New York"]
TERR = [("DUI / DWI","Orlando","FL",4,1),("Personal Injury","Miami","FL",3,0),("Family Law","Tampa","FL",3,0),("Criminal Defense","Jacksonville","FL",7,0),("Immigration","Austin","TX",1,0),("Bankruptcy","Los Angeles","CA",6,0),("Real Estate","New York","NY",2,0),("Bail Bonds","Fort Lauderdale","FL",0,0),("Criminal Defense","Orlando","FL",4,0),("Family Law","Miami","FL",5,0),("Personal Injury","Tampa","FL",4,0),("Immigration","Orlando","FL",2,0)]
QUESTIONS = [
 ("Can I refuse a breathalyzer in Florida without losing my license?","DUI / DWI","Orlando","FL","Tom Becker",3,412,"Answered","2 hours ago","Amir A. Ladan",True),
 ("Does my ex need my permission to move out of state with our kids?","Family Law","Miami","FL","Aisha Khan",2,268,"Answered","5 hours ago","Sarah J. Connor",False),
 ("Rear-ended at a red light. Insurance offered $1,800. Is that fair?","Personal Injury","Tampa","FL","Carlos Mendez",0,91,"Awaiting answer","40 minutes ago",None,False),
 ("My H-1B employer laid me off. How long do I have to find a new sponsor?","Immigration","Austin","TX","Priya Natarajan",1,530,"Answered","Yesterday","Maria E. Gonzalez",False),
 ("Will Chapter 7 wipe out my private student loans?","Bankruptcy","Los Angeles","CA","Kevin O'Neil",1,744,"Answered","2 days ago","David Kim",False),
 ("Is a first-offense DUI in Florida a felony or a misdemeanor?","DUI / DWI","Orlando","FL","Lucas Nguyen",4,1204,"Answered","3 days ago","John P. Morgan",True),
 ("How much does a DUI lawyer cost in Orlando?","DUI / DWI","Orlando","FL","Hannah Reed",6,2310,"Answered","1 week ago","Amir A. Ladan",False),
 ("Can I get a hardship license after a refusal?","DUI / DWI","Tampa","FL","Sofia Martins",2,388,"Answered","2 weeks ago","Maria E. Gonzalez",True),
 ("Will a DUI arrest show up on a background check if I'm not convicted?","Criminal Defense","Jacksonville","FL","Michael Turner",3,902,"Answered","3 weeks ago","Amir A. Ladan",False),
 ("Cheap loans click here!!! best rates guaranteed","—","—","","Victor Alves",0,0,"Hidden","Yesterday",None,False),
]
POSTS = [
 ("What to Do Immediately After a DUI Arrest in Florida","Criminal Defense","Amir A. Ladan","Oct 12, 2024","Published","9,306","5 min","https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&q=80&w=200"),
 ("Understanding Child Custody Laws: A Parent's Guide","Family Law","Sarah J. Connor","Oct 08, 2024","Published","4,812","6 min","https://images.unsplash.com/photo-1450101499163-c8848c66cb85?auto=format&fit=crop&q=80&w=200"),
 ("5 Common Legal Mistakes Startup Founders Make","Corporate Law","Michael T. Ross","Oct 05, 2024","Published","2,140","4 min","https://images.unsplash.com/photo-1505664194779-8beaceb93744?auto=format&fit=crop&q=80&w=200"),
 ("How to Avoid Traps When Buying Commercial Property","Real Estate","Jessica Pearson","Sep 28, 2024","Published","1,388","7 min",None),
 ("Do You Really Need a Lawyer After a Car Accident?","Personal Injury","Harvey Specter","Sep 20, 2024","Published","3,077","5 min",None),
 ("Changes to H-1B Visa Applications for 2025","Immigration","Elena Rodriguez","Sep 15, 2024","Published","2,655","4 min",None),
 ("How to Choose the Right Criminal Defense Attorney","Criminal Defense","Amir A. Ladan","Sep 10, 2024","Published","1,902","5 min",None),
 ("Understanding Bail and Bonds in the Florida System","Criminal Defense","Omar Haddad","Sep 02, 2024","Published","1,240","4 min",None),
 ("Misdemeanor vs. Felony: What Are the Real Differences?","Criminal Defense","Maria E. Gonzalez","Aug 26, 2024","Published","2,018","6 min",None),
 ("Understanding Implied Consent in Florida","Criminal Defense","Amir A. Ladan","Sep 16, 2026","Scheduled","—","5 min",None),
 ("Tenant Deposits: What Landlords Can and Cannot Deduct","Real Estate","Jessica Pearson","—","Draft","—","—",None),
]
BLOG_CATS = [("Criminal Defense",12),("Family Law",8),("Personal Injury",15),("Corporate Law",5),("Real Estate",9),("Immigration",4)]
TEAM = [("Bert Seale","Founder & CEO","28+ years across consulting, IT, startups and software. Inventor, author and the original architect of InKozi."),("Liza Seale","Co-Founder & President","Cybersecurity graduate and Orlando's 2020 Woman of the Year. Leads platform security and digital marketing."),("Chris Callaway","Chief Technology Officer","20+ years in technology. Owns the engineering roadmap and has shipped multiple startups alongside the founder."),("Dr. Sheffield Abood","Chief Financial Officer","Three decades as a physician turned finance lead, bringing 30+ years of accounting and business management."),("Paul Cella","Chief Executive Officer","Guides company strategy and partnerships as InKozi expands into new markets and professional categories."),("Bret Grubbs","National Sales Manager","25+ years of marketing with Fortune 500 experience, leading campaigns that drive growth and market expansion."),("Guido Gulla","VP, Operations","Runs talent, HR and administration, keeping national operations and the team engaged and moving."),("Michael Boggus","Chief Data Officer","Oversees data collection, management and analysis so every product decision is backed by evidence.")]
FAQ = {
 "For Users": [("What is InKozi?","InKozi is a technology platform that connects consumers with qualified, verified local attorneys and service providers."),("What happens when I submit a question?","Your question is automatically directed to qualifying local providers who have claimed your category and city."),("Is it safe to use InKozi?","Yes. Your personal information is protected behind a secure gateway and shared only with responding providers."),("Who are the attorneys that answer my question?","Every participating attorney is vetted: we verify their license and certifications, run a background check, and confirm good standing."),("Do the listed attorneys work for InKozi?","No. All providers are independent. They are not employed by or affiliated with InKozi."),("What does it cost me?","Nothing. Creating an account, asking questions and finding a lawyer on InKozi.com or the Ask KOZI app is completely free."),("How do I ask a question?","Register for free, choose a practice area, choose your location, then describe your situation."),("Which kinds of professionals are on InKozi?","Top-rated lawyers across 28+ practice areas, plus bail agents and chiropractors in many communities.")],
 "For Providers": [("How does a provider sign up?","Claim a practice category and city, verify your mobile number, and complete your profile. Approval takes about 48 hours."),("Why join InKozi?","Exclusive territories capped at seven providers, no pay-per-click, strong ROI, instant lead alerts, and no long-term contracts."),("What does it cost to join?","A one-time $375 administration and set-up fee, then $45 per month hosting for each category-and-city territory."),("Do I have to sign up for 12 months?","No. Hosting is pay-as-you-go in 30-day periods. It renews automatically each month, and you can cancel before any renewal."),("How are inquiries distributed?","The first provider in a territory receives every inquiry until a second slot is filled. After that, leads rotate evenly."),("Can I claim multiple categories and cities?","Yes, as many as you like. Each provider may hold only one of the seven slots per category per city."),("Does InKozi screen potential clients?","Yes. An AI-powered questionnaire in the intake flow filters inquiries so the leads that reach your dashboard are relevant."),("What is a custom provider URL?","Every approved provider gets a personalised, SEO-optimised URL on InKozi that ranks for your name, category and city."),("Can I get a refund on hosting?","No. Exposure begins the moment your profile goes live, so hosting fees are non-refundable."),("What else does InKozi offer providers?","Site blogging, social media management, phone and email services, and access to third-party financing resources.")],
 "For Affiliates": [("How does an affiliate sign up?","Claim your category and city just like a provider. Approval takes about 48 hours."),("Why become an InKozi affiliate?","Free brand promotion with no fees, plus community partnerships that help your business grow alongside related services."),("Why is it free?","Affiliate engagement lets InKozi connect users across multiple business streams, which is how we grow."),("How do I gain exposure?","A multi-tier system of digital marketing, cross-linking and deep linking connects your page to related services."),("Where will my page be displayed?","In the InKozi search database, by location and category, alongside relevant businesses and professionals.")],
}

def initials(name):
    p = [x for x in name.replace('.', '').replace('Dr', '').split() if x]
    return (p[0][0] + (p[-1][0] if len(p) > 1 else '')).upper()
def av(name, img=None, cls=''):
    return f'<img class="avatar {cls}" src="{img}" alt="{H.escape(name)}">' if img else f'<span class="avatar {cls}">{initials(name)}</span>'
def pav(name, cls=''):
    return av(name, PROV.get(name, (None,))[0], cls)
def who(name, sub, img=None, cls=''):
    return f'<div class="who">{av(name, img, cls)}<div><strong>{H.escape(name)}</strong><span>{sub}</span></div></div>'
def pwho(name, sub=None, cls=''):
    p = PROV[name]; return who(name, sub if sub is not None else f'{p[1]} · {p[2]}, {p[3]}', p[0], cls)
def uwho(name, sub=None, cls=''):
    u = USERS[name]; return who(name, sub if sub is not None else f'{u[0]}, {u[1]}', None, cls)
def pill(kind, text):
    return f'<span class="pill {kind}">{text}</span>'
def status_pill(s):
    m = {"Verified":"ok","Active":"ok","Published":"ok","Approved":"ok","Paid":"ok","Answered":"ok","Resolved":"ok","Live":"ok","Connected":"ok","Retained":"ok","Sent":"ok","Complete":"ok","Signed":"ok","Redeemed":"ok",
         "Pending":"warn","Awaiting answer":"warn","Scheduled":"warn","Unverified":"warn","Waiting":"warn","Reserved":"warn","Cancelling":"warn","Due":"warn","Unsigned":"warn","Queued":"warn","In review":"info","New":"info","Open":"info","Sending":"info",
         "Past due":"bad","Suspended":"bad","Flagged":"bad","Hidden":"bad","Failed":"bad","Reported":"bad","Rejected":"bad","Urgent":"bad","Expired":"bad",
         "Inactive":"","Draft":"","Closed":"","Refunded":"","Ended":"","Paused":""}
    return pill(m.get(s, ''), s)
def spark(points, color='#8c1fa9'):
    w, h = 96, 36; mn, mx = min(points), max(points); rng = (mx - mn) or 1
    pts = ['%.1f,%.1f' % (i * (w / (len(points) - 1)), h - 3 - (p - mn) / rng * (h - 6)) for i, p in enumerate(points)]
    line = ' '.join(pts); gid = 'g%d' % (abs(hash(line)) % 100000)
    return (f'<svg class="s-spark" viewBox="0 0 {w} {h}" preserveAspectRatio="none"><defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{color}" stop-opacity=".28"/><stop offset="1" stop-color="{color}" stop-opacity="0"/></linearGradient></defs>'
            f'<polygon points="0,{h} {line} {w},{h}" fill="url(#{gid})"/><polyline points="{line}" fill="none" stroke="{color}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/></svg>')
def stat(label, value, delta, up, icon, points, note='vs last 30 days'):
    d = 'up' if up else 'down'
    return (f'<div class="card stat"><div class="s-top"><span class="s-label">{label}</span><span class="s-icon"><i class="bi {icon}"></i></span></div>'
            f'<div class="s-value">{value}</div><div class="s-delta {d}"><i class="bi bi-arrow-{d}-right"></i> {delta} <span>{note}</span></div>{spark(points, "#16A34A" if up else "#E11D48")}</div>')
def card(title, body, tools='', hint='', foot='', cls=''):
    head = f'<div class="card-head"><h3>{title}{("<span class=\"hint\">%s</span>" % hint) if hint else ""}</h3><div class="tools">{tools}</div></div>' if title else ''
    return f'<div class="card {cls}">{head}{body}{("<div class=\"card-foot\">%s</div>" % foot) if foot else ""}</div>'
def pager(shown='1–10', total='248'):
    return (f'<div class="tbl-foot"><span>Showing <strong>{shown}</strong> of <strong>{total}</strong></span><div class="pager"><a href="#"><i class="bi bi-chevron-left"></i></a><a href="#" class="active">1</a><a href="#">2</a><a href="#">3</a><span>…</span><a href="#">25</a><a href="#"><i class="bi bi-chevron-right"></i></a></div></div>')
def table(cols, rows, checks=True, foot=True, shown='1–10', total='248', cls=''):
    th = '<th class="chk"><input class="form-check-input" type="checkbox" data-check-all aria-label="Select all"></th>' if checks else ''
    for c in cols:
        th += f'<th class="{c[1]}">{c[0]}</th>' if isinstance(c, tuple) else f'<th>{c}</th>'
    trs = ''
    for r in rows:
        tds = '<td class="chk"><input class="form-check-input" type="checkbox" aria-label="Select row"></td>' if checks else ''
        for i, cell in enumerate(r):
            c = cols[i]; k = f' class="{c[1]}"' if isinstance(c, tuple) and c[1] else ''
            tds += f'<td{k}>{cell}</td>'
        trs += f'<tr>{tds}</tr>'
    return f'<div class="table-wrap"><table class="tbl {cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>{pager(shown, total) if foot else ""}'
def row_actions(view='#', edit='#', more=None):
    more = more or [("bi-envelope","Send message","#"),("bi-slash-circle","Suspend","#"),("bi-trash","Delete","#")]
    items = ''.join(f'<li><a class="dropdown-item{" text-danger" if i == len(more) - 1 else ""}" href="{h}"><i class="bi {ic}"></i> {t}</a></li>' for i, (ic, t, h) in enumerate(more))
    return (f'<div class="actions"><a href="{view}" class="icon-btn" data-bs-toggle="tooltip" title="View"><i class="bi bi-eye"></i></a><a href="{edit}" class="icon-btn" data-bs-toggle="tooltip" title="Edit"><i class="bi bi-pencil"></i></a>'
            f'<div class="dropdown"><button class="icon-btn" data-bs-toggle="dropdown"><i class="bi bi-three-dots"></i></button><ul class="dropdown-menu dropdown-menu-end">{items}</ul></div></div>')
def filters(placeholder, selects=(), chips=(), extra=''):
    s = f'<div class="search"><i class="bi bi-search"></i><input type="search" placeholder="{placeholder}"></div>'
    for name, opts in selects:
        s += f'<select class="form-select" aria-label="{name}"><option>{name}</option>' + ''.join(f'<option>{o}</option>' for o in opts) + '</select>'
    if chips:
        s += '<div class="chips">' + ''.join(f'<span class="chip {"active" if i == 0 else ""}">{c}</span>' for i, c in enumerate(chips)) + '</div>'
    return f'<div class="filters">{s}<div class="spacer"></div>{extra}</div>'
def kv(pairs):
    return '<dl class="kv">' + ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in pairs) + '</dl>'
def timeline(items):
    return '<ul class="tl">' + ''.join(f'<li><span class="t-dot {kind}"><i class="bi {icon}"></i></span><div class="t-body">{text}<span class="t-time">{when}</span></div></li>' for icon, kind, text, when in items) + '</ul>'
def stars(n):
    full = int(n); half = 1 if n - full >= 0.5 else 0
    return '<span class="rating">' + '<i class="bi bi-star-fill"></i>' * full + ('<i class="bi bi-star-half"></i>' if half else '') + '<i class="bi bi-star"></i>' * (5 - full - half) + '</span>'
def switch(title, desc, on=True):
    return f'<div class="switch-row"><div><strong>{title}</strong><span>{desc}</span></div><div class="form-check form-switch"><input class="form-check-input" type="checkbox"{" checked" if on else ""}></div></div>'
def fld(label, control, hint='', small=''):
    return f'<div class="fld"><label>{label}{("<small>%s</small>" % small) if small else ""}</label>{control}{("<div class=\"hint\">%s</div>" % hint) if hint else ""}</div>'
def inp(value='', placeholder='', typ='text'):
    return f'<input class="form-control" type="{typ}" value="{H.escape(value)}" placeholder="{H.escape(placeholder)}">'
def textarea(value='', rows=3):
    return f'<textarea class="form-control" style="min-height:{rows * 28 + 24}px">{H.escape(value)}</textarea>'
def select(options, current=None):
    return '<select class="form-select">' + ''.join(f'<option{" selected" if o == current else ""}>{o}</option>' for o in options) + '</select>'
def steps(labels, active):
    return '<div class="steps">' + ''.join(f'<div class="st {"done" if i < active else ("active" if i == active else "")}"><div class="bar"></div><div class="lbl">{i + 1} · {l}</div></div>' for i, l in enumerate(labels)) + '</div>'
def stats_row(items):
    return '<div class="grid grid-4 mb-20">' + ''.join(stat(*i) for i in items) + '</div>'
def two_col(left, right, cls='grid-8-4'):
    return f'<div class="grid {cls}"><div>{left}</div><div>{right}</div></div>'

# ---------------- shell (multi-portal) ----------------
SITE = {}
def use_site(out, env, nav, user, search='Search…', create=None, public_link='../frontend/index.html', notif='notifications.html', profile='settings.html', logout='../frontend/login.html'):
    SITE.clear(); SITE.update(dict(out=out, env=env, nav=nav, user=user, search=search, create=create or [], public_link=public_link, notif=notif, profile=profile, logout=logout))
    os.makedirs(out, exist_ok=True)

def sidebar(active):
    nav = ''
    for label, items in SITE['nav']:
        nav += f'<div class="sb-label">{label}</div>'
        for href, icon, text, count in items:
            c = f'<span class="count{" hot" if count and "hot" in count else ""}">{count.replace(" hot", "")}</span>' if count else ''
            nav += f'<a href="{href}" class="sb-link{" active" if href == active else ""}"><i class="bi {icon}"></i> {text} {c}</a>'
    n, ini, role, img = SITE['user']
    a = f'<img class="avatar" src="{img}" alt="">' if img else f'<span class="avatar">{ini}</span>'
    return (f'<aside class="sidebar" id="sidebar"><div class="sb-brand"><a href="index.html"><img src="assets/images/logo.png" alt="InKozi"></a><span class="env">{SITE["env"]}</span><button class="sb-close" data-sb-close aria-label="Close menu"><i class="bi bi-x-lg"></i></button></div>'
            f'<nav class="sb-nav">{nav}</nav><div class="sb-foot"><a href="{SITE["profile"]}" class="sb-user">{a}<div><strong>{n}</strong><span>{role}</span></div><i class="bi bi-box-arrow-right out" title="Sign out"></i></a></div></aside><div class="sb-backdrop" data-sb-close></div>')

def topbar():
    n, ini, role, img = SITE['user']
    a = f'<img class="avatar" src="{img}" alt="">' if img else f'<span class="avatar">{ini}</span>'
    cr = SITE['create']
    if len(cr) == 1:
        h, i, l = cr[0]; create = f'<a href="{h}" class="btn-brand btn-sm"><i class="bi {i}"></i> {l}</a>'
    elif cr:
        create = '<div class="dropdown"><button class="btn-brand btn-sm" data-bs-toggle="dropdown"><i class="bi bi-plus-lg"></i> Create</button><ul class="dropdown-menu dropdown-menu-end">' + ''.join(f'<li><a class="dropdown-item" href="{h}"><i class="bi {i}"></i> {l}</a></li>' for h, i, l in cr) + '</ul></div>'
    else:
        create = ''
    return (f'<header class="topbar"><button class="tb-toggle" data-sb-toggle aria-label="Open menu"><i class="bi bi-list"></i></button>'
            f'<div class="tb-search"><i class="bi bi-search"></i><input type="search" placeholder="{SITE["search"]}"><kbd>⌘K</kbd></div><div class="tb-actions">{create}'
            f'<a href="{SITE["notif"]}" class="tb-btn" aria-label="Notifications"><i class="bi bi-bell"></i><span class="dot"></span></a>'
            f'<a href="{SITE["public_link"]}" target="_blank" class="tb-btn" aria-label="Open public site" data-bs-toggle="tooltip" title="Open public site"><i class="bi bi-box-arrow-up-right"></i></a><span class="tb-sep"></span>'
            f'<div class="dropdown"><div class="tb-user" data-bs-toggle="dropdown">{a}<div><div class="name">{n}</div><div class="role">{role}</div></div><i class="bi bi-chevron-down"></i></div>'
            f'<ul class="dropdown-menu dropdown-menu-end"><li><a class="dropdown-item" href="{SITE["profile"]}"><i class="bi bi-person"></i> My account</a></li><li><hr class="dropdown-divider"></li><li><a class="dropdown-item text-danger" href="{SITE["logout"]}"><i class="bi bi-box-arrow-right"></i> Sign out</a></li></ul></div></div></header>')

def head(title):
    return (f'<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="robots" content="noindex">\n  <title>{title} — InKozi {SITE["env"]}</title>\n'
            '  <link rel="icon" type="image/png" href="assets/images/favicon.png">\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">\n  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">\n  <link href="assets/css/admin.css" rel="stylesheet">\n</head>')
def scripts(charts=False, extra=''):
    s = '<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>'
    if charts: s += '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>'
    return s + '<script src="assets/js/admin.js"></script>' + extra
def shell(file, title, active, h1, body, sub='', crumbs=None, actions='', charts=False, extra_js=''):
    crumbs = crumbs or [("Dashboard", "index.html"), (h1, None)]
    cr = ''
    for i, (label, href) in enumerate(crumbs):
        if i: cr += '<i class="bi bi-chevron-right"></i>'
        cr += f'<a href="{href}">{label}</a>' if href else f'<span>{label}</span>'
    page = head(title) + '\n<body>\n<div class="app">\n' + sidebar(active) + '\n<div class="main">\n' + topbar() + '\n<main class="content">\n'
    page += f'<div class="page-head"><div><div class="crumbs">{cr}</div><h1>{h1}</h1>{("<div class=\"sub\">%s</div>" % sub) if sub else ""}</div>{("<div class=\"page-actions\">%s</div>" % actions) if actions else ""}</div>\n'
    page += body + '\n</main>\n</div>\n</div>\n' + scripts(charts, extra_js) + '\n</body>\n</html>\n'
    open(SITE['out'] + file, 'w').write(page)
    print('wrote', SITE['out'].rstrip('/').split('/')[-1] + '/' + file)
def standalone(file, title, body, extra_js=''):
    open(SITE['out'] + file, 'w').write(head(title) + '\n<body>\n' + body + '\n' + scripts(False, extra_js) + '\n</body>\n</html>\n')
    print('wrote', SITE['out'].rstrip('/').split('/')[-1] + '/' + file)
def use_admin():
    use_site(OUT, 'Admin', NAV, ('Liza Seale', 'LS', 'Co-Founder & President', None), 'Search users, providers, questions, territories…',
             [("providers.html","bi-briefcase","Add provider"),("territories.html","bi-pin-map","Open a territory"),("blog-editor.html","bi-journal-plus","New blog post"),("faq.html","bi-question-circle","New FAQ entry"),("team.html","bi-person-plus","Invite staff")],
             profile='profile.html', logout='login.html')
use_admin()
