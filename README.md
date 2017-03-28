     ___      ___         _       _
    | _ \_  _| _ \__ _ __| |_____| |_
    |  _/ || |  _/ _` / _| / / -_)  _|
    |_|  \_, |_| \__,_\__|_\_\___|\__|
         |__/

A simple CLI logger to receive and decode APRS packets via rtl_fm (RTL-SDR) and multimon-ng. This project serves as an open source expirimental tool for research into the RF spectrum and APRS.

## Requirements

Requires the following to be installed and configured on your system in order to run.

* Some form of Linux OS. MacOS, possibly. Windows, doubtful.
* An RTL-SDR compatible device.
* Python >= v3.5
* [rtl_fm](http://osmocom.org/projects/sdr/wiki/rtl-sdr)
* [multimon-ng](https://github.com/EliasOenal/multimon-ng)

At this time, you are on your own with regards to dependency setup. There are significant pieces of this which are hard coded and have no configurability options. See the Future Plans section for more info.

## Running

From the directory you've cloned the repository to, simply execute `python main.py`. The application will start and immediately begin listening on 144.39Mhz. Logged packets will be output to your terminal.

## Patch Notes

* 3/27/17
    * Restructured files to use proper Python module organization.
    * Basic framework for logging.
    * Resolved an exception involving unparseable decoded data.

## Future Plans

* APRS frame deserialization for human readability, likely.
* Simple TCP server (for use in Xastir etc.), likely.
* Command line configuration options for frequency, gain, definitely.
* Better documentation, definitely.
* Performance optimization, probably.
* Custom IGate uploading, maybe.

## Contributing

You are welcome to contribute by submitting pull requests on GitHub as you see fit!

## Credits

This project makes use of some code / inspiration from [pimultimonaprs](https://github.com/asdil12/pymultimonaprs) and as such, retains the GPLv3 license of its predecessor.
