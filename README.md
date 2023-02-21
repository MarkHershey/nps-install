# nps-install

Convenient install scripts for [`ehang-io / nps`](https://github.com/ehang-io/nps), an intranet penetration proxy server.

## Step 1: Setup NPS Server

## Step 2: Setup Clients

### 2.1: Create client entry in server configuration

### 2.2: Install client on client machine

At this point, you should have your server running with a fixed `ip` address and a `port` number, and obtained a new `vkey` for this new client machine.

Run the following command to install the nps client on the client machine

```bash
python3 client_install.py --server xxx.xxx.xxx.xxx --port xxxx --vkey xxxxxxxx
```

-   `--server` and `--vkey` arguments are always required.
-   `--port` is optional and default to `8024` if not specified.
