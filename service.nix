{ config, lib, pkgs, ... }:

let
  # The package itself. It resolves to the package installation directory.
  piLocalMqttClient = pkgs.callPackage ./default.nix {};

  # An object containing user configuration (in /etc/nixos/configuration.nix)
  cfg = config.services.pi-local-mqtt-client;
in {
  options.services.pi-local-mqtt-client.enable = lib.mkEnableOption "pi-local-mqtt-client";

  config = lib.mkIf cfg.enable {
    systemd.services.pi-local-mqtt-client = {
      description = "python client for publishing local info via mqtt";
      after = [ "network-online.target" ];
      wantedBy = [ "network-online.target" ];
      serviceConfig = {
        ExecStart = "${piLocalMqttClient}/bin/client";
        Restart = "always";
        RestartSec = "60";
        DynamicUser = "true";
        Group="i2c"; # script needs access to i2c interface
    };
    };
  };
}
