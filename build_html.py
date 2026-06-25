#!/usr/bin/env python3
"""Generate the Secure Pull Architecture HTML presentation."""

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Secure Pull Architecture - Animated Network Diagram</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:linear-gradient(135deg,#0d1b2a 0%,#1b2838 50%,#0d1b2a 100%);min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:20px;overflow-x:hidden}
.title-banner{background:linear-gradient(90deg,#00bceb,#0076d5);border-radius:50px;padding:15px 60px;margin-bottom:30px;box-shadow:0 4px 20px rgba(0,188,235,0.4);animation:pulseGlow 3s ease-in-out infinite}
.title-banner h1{color:#fff;font-size:2.2em;font-weight:700;text-align:center;letter-spacing:2px}
@keyframes pulseGlow{0%,100%{box-shadow:0 4px 20px rgba(0,188,235,0.4)}50%{box-shadow:0 4px 40px rgba(0,188,235,0.8)}}
.container{width:100%;max-width:1400px;position:relative}
.zone-badge{position:absolute;top:10px;padding:8px 20px;border-radius:8px;font-weight:700;font-size:0.9em;color:#fff;z-index:10}
.zone-dmz{right:20px;background:#00bceb}
.zone-dc{right:20px;background:#6cc04a;bottom:10px;top:auto}
.secure-pull-tag{position:fixed;top:20px;left:20px;background:rgba(0,0,0,0.7);border:2px solid #00bceb;border-radius:10px;padding:10px 15px;color:#00bceb;font-weight:700;font-size:0.85em;z-index:100;animation:pulseGlow 3s ease-in-out infinite}
.layer{position:relative;display:flex;align-items:center;padding:20px 20px 20px 150px;margin-bottom:4px;border-radius:12px;opacity:0;transform:translateX(-50px);animation:slideIn 0.8s ease forwards;min-height:130px}
.layer:nth-child(1){animation-delay:0.2s}
.layer:nth-child(3){animation-delay:0.4s}
.layer:nth-child(5){animation-delay:0.6s}
.layer:nth-child(7){animation-delay:0.8s}
.layer:nth-child(9){animation-delay:1.0s}
@keyframes slideIn{to{opacity:1;transform:translateX(0)}}
.layer-5{background:linear-gradient(90deg,rgba(220,53,69,0.15),rgba(220,53,69,0.05));border:1px solid rgba(220,53,69,0.3)}
.layer-4{background:linear-gradient(90deg,rgba(255,165,0,0.15),rgba(255,165,0,0.05));border:1px solid rgba(255,165,0,0.3)}
.layer-3{background:linear-gradient(90deg,rgba(0,188,235,0.15),rgba(0,188,235,0.05));border:1px solid rgba(0,188,235,0.3)}
.layer-2{background:linear-gradient(90deg,rgba(108,192,74,0.15),rgba(108,192,74,0.05));border:1px solid rgba(108,192,74,0.3)}
.layer-1{background:linear-gradient(90deg,rgba(108,192,74,0.2),rgba(108,192,74,0.08));border:1px solid rgba(108,192,74,0.4)}
.layer-badge{width:70px;height:70px;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;font-weight:700;margin-right:15px;flex-shrink:0;box-shadow:0 4px 15px rgba(0,0,0,0.3)}
.layer-badge .lbl{font-size:0.55em;opacity:0.9}
.layer-badge .num{font-size:1.4em;line-height:1}
.badge-red{background:linear-gradient(135deg,#dc3545,#a71d2a)}
.badge-orange{background:linear-gradient(135deg,#fd7e14,#e8590c)}
.badge-cyan{background:linear-gradient(135deg,#00bceb,#0076d5)}
.badge-green{background:linear-gradient(135deg,#6cc04a,#3d8b37)}
.badge-darkgreen{background:linear-gradient(135deg,#198754,#0f5132)}
.layer-title{font-size:1.3em;font-weight:700;color:#fff;min-width:130px;margin-right:10px}
.layer-content{display:flex;align-items:center;flex:1;justify-content:center}
.layer-details{color:rgba(255,255,255,0.85);font-size:0.8em;line-height:1.7;min-width:300px;margin-left:auto;padding-left:20px}
.layer-details li{list-style:none;padding-left:15px;position:relative}
.layer-details li::before{content:"\\2022";position:absolute;left:0;color:#00bceb}
.left-note{position:absolute;left:10px;top:50%;transform:translateY(-50%);background:rgba(0,188,235,0.08);border:1px solid rgba(0,188,235,0.25);border-radius:8px;padding:8px 10px;color:rgba(255,255,255,0.65);font-size:0.65em;font-style:italic;max-width:125px;text-align:center}
.conn-svg{display:block;width:100%;height:28px;overflow:visible}
.icon-fw{width:55px;height:55px;position:relative;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0}
.icon-fw::before{content:'';width:48px;height:48px;background:linear-gradient(135deg,#dc3545,#a71d2a);border-radius:4px;position:absolute}
.icon-fw::after{content:'';width:35px;height:3px;background:#fff;position:absolute;box-shadow:0 8px 0 #fff,0 -8px 0 #fff}
.icon-proxy{width:55px;height:55px;background:linear-gradient(135deg,#fd7e14,#e8590c);border-radius:50%;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:0.6em;text-align:center;line-height:1.2;flex-shrink:0}
.icon-server{width:45px;height:55px;position:relative;display:inline-flex;flex-shrink:0}
.icon-server::before{content:'';width:45px;height:50px;background:linear-gradient(180deg,#2196F3,#1565C0);border-radius:4px;position:absolute;top:0;left:0}
.icon-server::after{content:'';width:28px;height:3px;background:rgba(255,255,255,0.7);position:absolute;top:10px;left:8px;box-shadow:0 10px 0 rgba(255,255,255,0.7),0 20px 0 rgba(255,255,255,0.7)}
.icon-switch{width:65px;height:28px;background:linear-gradient(90deg,#0076d5,#00bceb);border-radius:4px;position:relative;display:inline-flex;flex-shrink:0}
.icon-switch::after{content:'';width:5px;height:5px;background:#6cc04a;border-radius:50%;position:absolute;top:50%;left:8px;transform:translateY(-50%);box-shadow:10px 0 0 #6cc04a,20px 0 0 #6cc04a,30px 0 0 #fd7e14,40px 0 0 #6cc04a}
.icon-cloud{width:65px;height:42px;background:rgba(0,188,235,0.15);border:2px solid #00bceb;border-radius:22px;display:inline-flex;align-items:center;justify-content:center;color:#00bceb;font-size:0.7em;font-weight:600;flex-shrink:0}
.icon-aci{width:55px;height:55px;border:3px solid #6cc04a;border-radius:50%;display:inline-flex;align-items:center;justify-content:center;flex-shrink:0;color:#6cc04a;font-size:0.55em;font-weight:700}
.icon-vm{width:42px;height:42px;background:linear-gradient(135deg,#00bceb,#0076d5);border-radius:8px;display:inline-flex;align-items:center;justify-content:center;color:#fff;font-size:0.65em;font-weight:700;flex-shrink:0}
.flow-svg{margin:0 8px;overflow:visible;flex-shrink:0}
#particles{position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:0}
.particle{position:absolute;border-radius:50%;animation:pfloat 15s ease-in-out infinite}
@keyframes pfloat{0%,100%{transform:translate(0,0) scale(1)}25%{transform:translate(20px,-20px) scale(1.3)}50%{transform:translate(-15px,25px) scale(0.7)}75%{transform:translate(18px,10px) scale(1.1)}}
@media(max-width:1200px){.layer{flex-wrap:wrap;padding-left:20px}.layer-details{min-width:200px}.left-note{display:none}}
</style>
</head>
<body>
<div class="secure-pull-tag">SECURE PULL</div>
<div class="title-banner"><h1>Secure Pull Architecture</h1></div>
<div class="container">
<div class="zone-badge zone-dmz">DMZ</div>

<!-- LAYER 5: Internet Firewall (Palo Alto) -->
<div class="layer layer-5">
<div class="layer-badge badge-red"><span class="lbl">LAYER</span><span class="num">5</span></div>
<div class="layer-title">Internet<br>Firewall</div>
<div class="layer-content">
<div class="icon-cloud">Internet</div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#fd7e14" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="4" fill="#fd7e14"><animateMotion path="M0,20 L80,20" dur="1.5s" repeatCount="indefinite"/></circle></svg>
<div class="icon-fw"></div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#00bceb" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="4" fill="#00bceb"><animateMotion path="M0,20 L80,20" dur="1.8s" repeatCount="indefinite"/></circle></svg>
<div class="icon-server"></div>
</div>
<div class="layer-details">
<li>Source IP Whitelisting &ndash; Only from Web Proxy</li>
<li>Destination Server IP &amp; URL Whitelisting</li>
<li>IPS, Web Filtering &amp; Anti-malware Security</li>
<li>Zoning &amp; Multi-tenancy</li>
<li>Unidirectional Flow</li>
</div>
</div>

<!-- Connection L5-L4 -->
<svg class="conn-svg"><line x1="50%" y1="0" x2="50%" y2="28" stroke="#fd7e14" stroke-width="2" stroke-dasharray="4,4"><animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#fd7e14"><animateMotion path="M 700,0 L 700,28" dur="1s" repeatCount="indefinite"/></circle><text x="52%" y="16" fill="rgba(255,255,255,0.5)" font-size="9" font-weight="600">Proxy</text></svg>

<!-- LAYER 4: Web Proxy -->
<div class="layer layer-4">
<div class="left-note">Only Proxy can communicate unidirectionally with Internet</div>
<div class="layer-badge badge-orange"><span class="lbl">LAYER</span><span class="num">4</span></div>
<div class="layer-title">Web<br>Proxy</div>
<div class="layer-content">
<div class="icon-proxy">WWW<br>Proxy</div>
<svg class="flow-svg" width="100" height="40"><line x1="0" y1="20" x2="100" y2="20" stroke="#fd7e14" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="0.8s" repeatCount="indefinite"/></line><circle r="4" fill="#fd7e14"><animateMotion path="M0,20 L100,20" dur="2s" repeatCount="indefinite"/></circle><circle r="3" fill="#6cc04a"><animateMotion path="M0,20 L100,20" dur="2s" begin="0.7s" repeatCount="indefinite"/></circle></svg>
<div class="icon-server"></div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#00bceb" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#00bceb"><animateMotion path="M0,20 L80,20" dur="1.5s" repeatCount="indefinite"/></circle></svg>
<div class="icon-vm"></div>
</div>
<div class="layer-details">
<li>Source IP Whitelisting &ndash; Only from Specific DMZ Servers</li>
<li>Destination Server IP &amp; URL Whitelisting</li>
<li>Web Reputation &amp; Web Usage Control</li>
<li>Anti-malware Analysis &amp; HTTPS Inspection</li>
</div>
</div>

<!-- Connection L4-L3 -->
<svg class="conn-svg"><line x1="50%" y1="0" x2="50%" y2="28" stroke="#00bceb" stroke-width="2" stroke-dasharray="4,4"><animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#00bceb"><animateMotion path="M 700,0 L 700,28" dur="1.2s" repeatCount="indefinite"/></circle><text x="52%" y="16" fill="rgba(255,255,255,0.5)" font-size="9" font-weight="600">Proxy</text></svg>

<!-- LAYER 3: DMZ Firewall -->
<div class="layer layer-3">
<div class="left-note">Only specific DMZ servers can communicate unidirectionally with Proxy</div>
<div class="layer-badge badge-cyan"><span class="lbl">LAYER</span><span class="num">3</span></div>
<div class="layer-title">DMZ<br>Firewall</div>
<div class="layer-content">
<div class="icon-fw"></div>
<svg class="flow-svg" width="90" height="40"><line x1="0" y1="20" x2="90" y2="20" stroke="#00bceb" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="0.9s" repeatCount="indefinite"/></line><circle r="4" fill="#00bceb"><animateMotion path="M0,20 L90,20" dur="1.5s" repeatCount="indefinite"/></circle><circle r="3" fill="#6cc04a"><animateMotion path="M0,20 L90,20" dur="1.5s" begin="0.5s" repeatCount="indefinite"/></circle></svg>
<div class="icon-switch"></div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#6cc04a" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#6cc04a"><animateMotion path="M0,20 L80,20" dur="1.2s" repeatCount="indefinite"/></circle></svg>
<div class="icon-vm"></div>
</div>
<div class="layer-details">
<li>Source IP Whitelisting &ndash; Only from Specific DMZ Servers</li>
<li>Destination Server IP &amp; URL Whitelisting</li>
<li>IPS, Web Filtering &amp; Anti-malware Security</li>
<li>Zoning &amp; Unidirectional Flow</li>
</div>
</div>

<!-- Connection L3-L2 -->
<svg class="conn-svg"><line x1="50%" y1="0" x2="50%" y2="28" stroke="#6cc04a" stroke-width="2" stroke-dasharray="4,4"><animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#6cc04a"><animateMotion path="M 700,0 L 700,28" dur="1s" repeatCount="indefinite"/></circle><text x="52%" y="16" fill="rgba(255,255,255,0.5)" font-size="9" font-weight="600">DC</text></svg>

<!-- LAYER 2: DC Firewall -->
<div class="layer layer-2">
<div class="layer-badge badge-green"><span class="lbl">LAYER</span><span class="num">2</span></div>
<div class="layer-title">DC<br>Firewall</div>
<div class="layer-content">
<div class="icon-fw"></div>
<svg class="flow-svg" width="110" height="40"><line x1="0" y1="20" x2="110" y2="20" stroke="#6cc04a" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="0.8s" repeatCount="indefinite"/></line><circle r="4" fill="#6cc04a"><animateMotion path="M0,20 L110,20" dur="1.8s" repeatCount="indefinite"/></circle><circle r="3" fill="#00bceb"><animateMotion path="M110,20 L0,20" dur="2s" repeatCount="indefinite"/></circle></svg>
<div class="icon-switch"></div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#6cc04a" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#6cc04a"><animateMotion path="M0,20 L80,20" dur="1.5s" repeatCount="indefinite"/></circle></svg>
<div class="icon-server"></div>
</div>
<div class="layer-details">
<li>Source &amp; Destination Server IP Whitelisting</li>
<li>Only from Specific Server to Specific DMZ Server</li>
<li>IPS, Zoning &amp; Multi-Instance</li>
<li>Unidirectional Flow from DC to DMZ</li>
</div>
</div>

<!-- Connection L2-L1 -->
<svg class="conn-svg"><line x1="50%" y1="0" x2="50%" y2="28" stroke="#6cc04a" stroke-width="2" stroke-dasharray="4,4"><animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#6cc04a"><animateMotion path="M 700,0 L 700,28" dur="1.2s" repeatCount="indefinite"/></circle></svg>

<!-- LAYER 1: ACI -->
<div class="layer layer-1">
<div class="left-note">Only specific DC servers can communicate unidirectionally with DMZ Servers</div>
<div class="layer-badge badge-darkgreen"><span class="lbl">LAYER</span><span class="num">1</span></div>
<div class="layer-title">ACI</div>
<div class="layer-content">
<div class="icon-aci">APIC</div>
<svg class="flow-svg" width="100" height="40"><line x1="0" y1="20" x2="100" y2="20" stroke="#6cc04a" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="0.7s" repeatCount="indefinite"/></line><circle r="4" fill="#6cc04a"><animateMotion path="M0,20 L100,20" dur="1.5s" repeatCount="indefinite"/></circle><circle r="3" fill="#198754"><animateMotion path="M0,20 L100,20" dur="1.5s" begin="0.5s" repeatCount="indefinite"/></circle></svg>
<div class="icon-switch"></div>
<svg class="flow-svg" width="80" height="40"><line x1="0" y1="20" x2="80" y2="20" stroke="#198754" stroke-width="2" stroke-dasharray="5,5"><animate attributeName="stroke-dashoffset" values="0;-20" dur="1s" repeatCount="indefinite"/></line><circle r="3" fill="#198754"><animateMotion path="M0,20 L80,20" dur="1.2s" repeatCount="indefinite"/></circle></svg>
<div class="icon-vm"></div>
</div>
<div class="layer-details">
<li>Source Whitelisting &ndash; Only from specific EPG to DMZ</li>
<li>Service Graphs, PBR, VRFs</li>
<li>EPGs, ESGs &amp; Multi-tenancy</li>
<li>Unidirectional Flow from EPG to DMZ</li>
</div>
</div>

<div class="zone-badge zone-dc">DC</div>
</div>

<div id="particles"></div>
<script>
(function(){
var c=document.getElementById('particles'),cols=['#00bceb','#6cc04a','#fd7e14','#dc3545'];
for(var i=0;i<25;i++){var p=document.createElement('div');p.className='particle';var s=Math.random()*4+2;p.style.cssText='width:'+s+'px;height:'+s+'px;background:'+cols[Math.floor(Math.random()*cols.length)]+';top:'+Math.random()*100+'vh;left:'+Math.random()*100+'vw;opacity:'+(Math.random()*0.25+0.05)+';animation-delay:'+Math.random()*8+'s;animation-duration:'+(Math.random()*12+10)+'s;';c.appendChild(p);}
})();
</script>
</body>
</html>
'''

with open('/projects/sandbox/Secure-Pull/index.html', 'w') as f:
    f.write(html_content)

print("HTML file created successfully!")
