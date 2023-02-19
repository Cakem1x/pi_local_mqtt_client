{ nixpkgs ? import <nixpkgs> {}, pythonPkgs ? nixpkgs.pkgs.python3Packages }:

let
  inherit (nixpkgs) pkgs;
  inherit pythonPkgs;
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.5.0";
  }) {};

  f = { }:
    mach-nix.buildPythonPackage rec {
      pname = "pi_local_mqtt_client";
      version = "0.0.1";

      src = ./.;
      requirements = builtins.readFile ./requirements.txt ;

      # no tests
      doCheck = false;

      # Meta information for the package
      meta = {
        description = "Simple python script that publishes data to mqtt";
      };
    };

  drv = pythonPkgs.callPackage f {};
in
  if pkgs.lib.inNixShell then drv else drv
