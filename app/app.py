import os

from flask import Flask, Response

APP_VERSION= os.environ.get("APP_VERSION", "0.0.1")


app = Flask(__name__)


LANDING_PAGE = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="theme-color" content="#170d2c">
    <title>Mentee Robotics — Built to move us forward</title>
    <style>
      :root {
        color-scheme: dark;
        font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        background: #10091e;
        color: #f7f3ff;
        font-synthesis: none;
        text-rendering: optimizeLegibility;
      }

      * { box-sizing: border-box; }
      body { margin: 0; min-width: 320px; }
      a { color: inherit; text-decoration: none; }
      .page { min-height: 100vh; overflow: hidden; background: radial-gradient(ellipse at 74% 44%, #321858 0, #190f2b 34%, #10091e 70%); }
      .shell { width: min(1160px, calc(100% - 48px)); margin: 0 auto; }
      header { height: 88px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid #ffffff16; }
      .brand { display: flex; align-items: center; gap: 12px; font-size: 15px; font-weight: 700; letter-spacing: .04em; }
      .brand-mark { width: 35px; height: 35px; display: grid; place-items: center; border: 1px solid #c5a5ff85; border-radius: 12px; color: #d7c0ff; background: #8d5be82b; font-size: 19px; }
      nav { display: flex; align-items: center; gap: 32px; color: #c9c0d8; font-size: 13px; }
      nav a:hover { color: white; }
      .nav-cta { padding: 11px 17px; border: 1px solid #b695ec75; border-radius: 7px; color: #f4edff; }
      main { min-height: calc(100vh - 89px); display: grid; grid-template-columns: 1fr 1fr; align-items: center; gap: 28px; padding: 72px 0 90px; }
      .eyebrow { display: flex; align-items: center; gap: 10px; color: #c5a5ff; font-size: 11px; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
      .eyebrow::before { content: ""; width: 25px; height: 1px; background: #b995f7; }
      h1 { max-width: 590px; margin: 23px 0 20px; font-size: clamp(48px, 6vw, 76px); line-height: .99; letter-spacing: -.065em; }
      h1 span { color: #c5a5ff; }
      .intro { max-width: 470px; color: #b8aec8; font-size: 16px; line-height: 1.8; }
      .actions { display: flex; align-items: center; gap: 24px; margin-top: 32px; }
      .button { padding: 14px 20px; border-radius: 7px; background: #a77af2; color: #170d2c; font-size: 13px; font-weight: 750; box-shadow: 0 8px 30px #9a66ed38; }
      .button:hover { background: #c5a5ff; }
      .text-link { color: #e3d9f3; font-size: 13px; }
      .text-link span { margin-left: 7px; color: #c5a5ff; }
      .visual { position: relative; min-height: 500px; display: grid; place-items: center; }
      .orbit { position: absolute; width: min(430px, 90%); aspect-ratio: 1; border: 1px solid #bd9cf322; border-radius: 50%; box-shadow: 0 0 100px #9f6be91b, inset 0 0 70px #9f6be90d; }
      .orbit::before, .orbit::after { content: ""; position: absolute; border: 1px solid #bd9cf31d; border-radius: 50%; }
      .orbit::before { inset: 9%; }
      .orbit::after { inset: 19%; }
      .glow { position: absolute; width: 235px; height: 300px; border-radius: 50%; background: #8b50ed30; filter: blur(55px); }
      .robot { position: relative; width: min(340px, 75%); z-index: 1; filter: drop-shadow(0 22px 40px #09051199); }
      .robot-note { position: absolute; right: 0; bottom: 34px; padding: 14px 17px; border: 1px solid #ffffff20; border-radius: 10px; background: #1b1229c9; backdrop-filter: blur(12px); }
      .robot-note strong { display: block; font-size: 12px; }
      .robot-note small { display: block; margin-top: 5px; color: #a99dbb; font-size: 10px; letter-spacing: .08em; }
      .version { position: absolute; left: 0; bottom: 35px; color: #786d88; font-size: 11px; }
      @media (max-width: 760px) {
        .shell { width: min(100% - 36px, 560px); }
        header { height: 72px; }
        nav a:not(.nav-cta) { display: none; }
        nav { gap: 0; }
        main { grid-template-columns: 1fr; gap: 0; padding: 70px 0 65px; }
        h1 { font-size: clamp(48px, 13vw, 68px); }
        .visual { min-height: 390px; margin-top: 5px; }
        .robot-note { right: 0; bottom: 20px; }
        .version { bottom: 20px; }
      }
      @media (prefers-reduced-motion: no-preference) {
        .robot { animation: hover 5s ease-in-out infinite; }
        @keyframes hover { 50% { transform: translateY(-9px); } }
      }
    </style>
  </head>
  <body>
    <div class="page">
      <div class="shell">
        <header>
          <a class="brand" href="/" aria-label="Mentee Robotics home">
            <span class="brand-mark" aria-hidden="true">M</span>
            <span>MENTEE ROBOTICS</span>
          </a>
          <nav aria-label="Main navigation">
            <a href="#vision">Our vision</a>
            <a href="#robots">Our robots</a>
            <a class="nav-cta" href="mailto:hello@menteerobotics.com">Get in touch</a>
          </nav>
        </header>
        <main id="vision">
          <section>
            <div class="eyebrow">A new kind of capable</div>
            <h1>Made for the<br>world we <span>share.</span></h1>
            <p class="intro">We build humanoid robots designed to work alongside people—bringing intelligence, dexterity, and a little more possibility into everyday life.</p>
            <div class="actions">
              <a class="button" href="#robots">Meet our robots</a>
              <a class="text-link" href="mailto:hello@menteerobotics.com">Discover Mentee <span aria-hidden="true">↗</span></a>
            </div>
          </section>
          <section class="visual" id="robots" aria-label="Mentee humanoid robot concept">
            <div class="orbit" aria-hidden="true"></div>
            <div class="glow" aria-hidden="true"></div>
            <svg class="robot" viewBox="0 0 340 470" role="img" aria-labelledby="robot-title">
              <title id="robot-title">A humanoid robot built by Mentee Robotics</title>
              <defs>
                <linearGradient id="shell" x1="0" x2="1" y1="0" y2="1">
                  <stop stop-color="#f0e9fa"/>
                  <stop offset=".48" stop-color="#bcb0d2"/>
                  <stop offset="1" stop-color="#796b98"/>
                </linearGradient>
                <linearGradient id="joint" x1="0" x2="1" y1="0" y2="1">
                  <stop stop-color="#b58aff"/>
                  <stop offset="1" stop-color="#7042b8"/>
                </linearGradient>
              </defs>
              <ellipse cx="171" cy="447" rx="83" ry="12" fill="#080512" opacity=".55"/>
              <path d="M142 157h56l13 39-41 28-41-28z" fill="url(#joint)" stroke="#d8c8f4" stroke-opacity=".55"/>
              <path d="M124 207q46-24 92 0l24 111q-70 31-140 0z" fill="url(#shell)" stroke="#f4eeff" stroke-opacity=".75" stroke-width="2"/>
              <path d="M134 222q37-15 72 0l-7 54q-29 12-58 0z" fill="#33234e"/>
              <path d="M144 237h52v6h-52z" rx="3" fill="#bd9bfa"/>
              <path d="M147 253h46v4h-46z" fill="#8565b5"/>
              <path d="M125 213 99 228l-28 91 18 7 42-78M215 213l26 15 28 91-18 7-42-78" fill="url(#shell)" stroke="#e8dff8" stroke-opacity=".7" stroke-width="2"/>
              <circle cx="80" cy="325" r="13" fill="url(#joint)"/>
              <circle cx="261" cy="325" r="13" fill="url(#joint)"/>
              <path d="m71 331-11 38 11 15 19-7 3-28zM270 331l11 38-11 15-19-7-3-28z" fill="url(#shell)" stroke="#e8dff8" stroke-opacity=".7" stroke-width="2"/>
              <path d="M144 316h52l8 29h-68z" fill="url(#joint)" stroke="#d8c8f4" stroke-opacity=".6"/>
              <path d="m138 339 33 11 33-11 10 84q-43 21-86 0z" fill="url(#shell)" stroke="#f4eeff" stroke-opacity=".75" stroke-width="2"/>
              <path d="m144 349 27 9v61l-30 5zM198 349l-27 9v61l30 5z" fill="#a89bbd"/>
              <path d="M142 419h30l-2 17q-14 9-39 4l1-8zM171 419h30l10 13 1 8q-25 5-39-4z" fill="#c7bbda"/>
              <path d="M126 72q45-30 90 0l-7 80q-38 27-76 0z" fill="url(#shell)" stroke="#f4eeff" stroke-opacity=".8" stroke-width="2"/>
              <path d="M126 92q45-23 90 0l-3 31q-42 20-84 0z" fill="#211632"/>
              <path d="M142 107h15v5h-15zM185 107h15v5h-15z" rx="2" fill="#c2a1ff"/>
              <path d="M151 137q20 10 40 0" fill="none" stroke="#8c7aa7" stroke-width="3" stroke-linecap="round"/>
              <path d="M158 67v-12q12-9 24 0v12" fill="none" stroke="#d7c8ee" stroke-width="5" stroke-linecap="round"/>
              <circle cx="170" cy="48" r="5" fill="#bc98ff"/>
              <circle cx="170" cy="196" r="5" fill="#d9c1ff"/>
            </svg>
            <div class="robot-note"><strong>Built around people</strong><small>HUMANOID ROBOTICS · HUMAN FUTURES</small></div>
          </section>
          <small class="version">Mentee Robotics · v__APP_VERSION__</small>
        </main>
      </div>
    </div>
  </body>
</html>
"""


@app.get("/")
def landing_page():
    return Response(
        LANDING_PAGE.replace("__APP_VERSION__", APP_VERSION),
        mimetype="text/html",
    )


@app.get("/health")
def health():
    return Response("ok\n", mimetype="text/plain")


@app.errorhandler(404)
def not_found(_error):
    return Response("Page not found\n", status=404, mimetype="text/plain")


@app.errorhandler(405)
def method_not_allowed(_error):
    return Response(
        "Method not allowed\n",
        status=405,
        headers={"Allow": "GET, HEAD"},
        mimetype="text/plain",
    )


# Keep the previous WSGI entry-point name available for existing deployments.
application = app


def main():
    port = int(os.environ.get("PORT", "8000"))
    print(f"Mentee Robotics landing page v{APP_VERSION} listening on port {port}")
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()

