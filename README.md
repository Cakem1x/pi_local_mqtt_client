This repo contains a simple MQTT client for communicating with my Raspberry Pi.
The Pi is used in a smart home project, published data includes BMP280 sensor and some stats like CPU temperature etc.

On Nix, you can run the client in a nix-shell via `nix-shell nix_env/ --command "python client.py"`.
