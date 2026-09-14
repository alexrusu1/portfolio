#!/usr/bin/env python3
"""Local dev server for the portfolio.

Run button (Code Runner) points here. Serves this folder over http://localhost
so the 3D .glb models load (browsers block file:// fetches), then opens the
site in your default browser. Press Ctrl+C in the terminal to stop.
"""
import http.server
import os
import socketserver
import sys
import threading
import webbrowser

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))
URL = f"http://localhost:{PORT}/index.html"
open_browser = "--no-open" not in sys.argv


def main():
    try:
        httpd = socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler)
    except OSError:
        # Port already in use — a server is likely running from a previous click.
        print(f"A server is already running on port {PORT}.")
        if open_browser:
            webbrowser.open(URL)
        return

    print(f"Serving {os.getcwd()}")
    print(f"  -> {URL}   (Ctrl+C to stop)")
    if open_browser:
        threading.Timer(0.6, lambda: webbrowser.open(URL)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        httpd.shutdown()


if __name__ == "__main__":
    main()
