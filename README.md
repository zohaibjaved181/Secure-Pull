# Secure Pull Architecture

## Overview

The **Secure Pull Architecture** is a multi-layer security design that enforces unidirectional traffic flow through five distinct security layers. This architecture ensures defense-in-depth by implementing strict IP whitelisting, zone-based segmentation, and comprehensive threat inspection at each layer.

## Architecture Layers

| Layer | Component | Function |
|-------|-----------|----------|
| **Layer 5** | Internet Firewall (Palo Alto) | Handles internet-facing traffic with IPS, web filtering, and anti-malware |
| **Layer 4** | Web Proxy | URL filtering, web reputation, HTTPS inspection, anti-malware analysis |
| **Layer 3** | DMZ Firewall | Protects DMZ VMs, enforces zoning and unidirectional flow |
| **Layer 2** | DC Firewall | Manages datacenter internal communication with multi-instance support |
| **Layer 1** | ACI (Cisco) | Micro-segmentation via EPGs, service graphs, PBR, and VRFs |

## Key Security Principles

- **Unidirectional Flow**: Traffic flows in one direction only between layers
- **IP Whitelisting**: Source and destination IP restrictions at every layer
- **Zone-Based Segmentation**: Strict isolation between DMZ and DC zones
- **Defense-in-Depth**: Multiple layers of inspection and filtering

## Files

- **`index.html`** - Interactive animated HTML presentation with real-time traffic flow visualization
- **`Secure_Pull_Architecture.pptx`** - PowerPoint presentation for offline viewing and sharing
- **`build_html.py`** - Python script to regenerate the HTML presentation
- **`build_pptx.py`** - Python script to regenerate the PPTX presentation

## Viewing the Presentation

### HTML (Recommended)
Open `index.html` in any modern web browser to see the animated architecture diagram with:
- Animated traffic flow particles showing real data movement
- Cisco SAFE-style network icons
- Layer-by-layer slide-in animations
- Floating background particles for visual appeal

### PowerPoint
Open `Secure_Pull_Architecture.pptx` in Microsoft PowerPoint or compatible application for:
- Static architecture diagram suitable for presentations
- Detailed traffic flow explanations
- Print-friendly format

## Traffic Flow

```
Internet --> [Palo Alto FW] --> [Web Proxy] --> [DMZ FW] --> [DC FW] --> [ACI/APIC]
   Layer 5       Layer 4         Layer 3       Layer 2      Layer 1
```

All traffic passes through proxy servers and is inspected at each layer boundary.
