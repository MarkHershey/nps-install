# nps-install

Convenient install scripts for [`ehang-io / nps`](https://github.com/ehang-io/nps), an intranet penetration proxy server.

## Step 1: Setup NPS Server

Download and install the nps server at a virtual machine with a fixed IP address.

-   default web interface will be served at port `8080`.
-   default client connection port at server side is `8024`.

## Step 2: Setup Clients

### 2.1: Create client entry in server configuration

-   Create a new `client` on the web interface. Just fill in the `remarks` input box should be suffice. `vkey` will be automatically generated.
-   Note down the generated `vkey` for the next step.

### 2.2: Install client on client machine

At this point, you should have your server running with a fixed `ip` address and a `port` number, and obtained a new `vkey` for this new client machine.

Run the following command to install the nps client on the client machine

```bash
python3 client_install.py --server xxx.xxx.xxx.xxx --port xxxx --vkey xxxxxxxx
```

-   `--server` and `--vkey` arguments are always required.
-   `--port` is optional and default to `8024` if not specified.

Successful installation will be reflected on the web interface as a new online client.

If not, check if the port for connection client and server (`8024`) at the server side is open for traffic.

```bash
sudo ufw allow
sudo ufw show added
sudo ufw enable
```

### 2.3 Setup penetration service

At this step, the port numbers may be slightly confusing, so take a breath. For example, we want to expose a client's SSH service to the public network. We have the following steps:

1. Make sure the SSH service is up and running in the client machine. The default port for `ssh` is `22`, but you may specify it to be otherwise.
2. For SSH service, we will use a TCP connection between the client machine and the nps server. Hence, we go to the web interface of nps, under `TCP` tab, we click the `+Add` button.
    - `Client ID` can be found in the `client` tab, it is an auto-generated integer.
    - `Server Port` will be a new unoccupied port on the server that you intent to allocate it to this client's service.
    - `Target (IP:Port)` will be the address of the client service at the client's subnet. For example, for default ssh service, it will be at `localhost:22`.
    - click `Add` button to save.
3. Important: Make sure that on the server machine, firewall is configured appropriately to allow two-way traffic on the new `Server Port` mentioned above.
4. Once all is done, test the connection at `AAAAAAA:BBBB` where `AAAAAAA` is the ip address of the nps server and `BBBB` is the `Server Port` specified above.

Congrats, that's all.
