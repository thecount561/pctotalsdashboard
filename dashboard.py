import dash
from dash.dependencies import Input, Output
from dash import dcc, html

cpus = {'7800x3d':['7800x3d','449.99','https://www.microcenter.com/product/674503/amd-ryzen-7-7800x3d-raphael-am5-42ghz-8-core-boxed-processor-heatsink-not-included'],
        '9800x3d':['9800x3d', '479.99', 'https://www.microcenter.com/product/687907/amd-ryzen-7-9800x3d-granite-ridge-am5-470ghz-8-core-boxed-processor-heatsink-not-included'],
        '5700x3d':['5700x3d', '179.99(sale)', 'https://www.microcenter.com/product/676051/amd-ryzen-7-5700x3d-vermeer-am4-30ghz-8-core-boxed-processor-heatsink-not-included'],
        '7600x3d':['7600x3d', '299.99(sale)', 'https://www.microcenter.com/product/684484/amd-ryzen-5-7600x3d-raphael-am5-41ghz-6-core-boxed-processor-heatsink-not-included'],
        'i7-14700k':['i7-14700k', '319.99(sale)', 'https://www.microcenter.com/product/670842/intel-core-i7-14700k-raptor-lake-34ghz-twenty-core-lga-1700-boxed-processor-heatsink-not-included'],
        'Ultra 7 265K':['Ultra 7 265K', '299.99(sale)', 'https://www.microcenter.com/product/685301/intel-core-ultra-7-265k-arrow-lake-twenty-core-lga-1851-boxed-processor-heatsink-not-included'],
        'i9-12900k':['i9-12900k', '249.99(sale)', 'https://www.microcenter.com/product/641915/intel-core-i9-12900k-alder-lake-32ghz-sixteen-core-lga-1700-boxed-processor-heatsink-not-included']}
mbs =  {'ASRock X870 Pro RS WiFi': ['ASRock X870 Pro RS WiFi', '209.99', 'https://www.microcenter.com/product/685301/asrock-x870-pro-rs-wifi-amd-am5-atx-motherboard'],
        'ASUS B650-PLUS TUF GAMING WIFI': ['ASUS B650-PLUS TUF GAMING WIFI', '179.99(sale)', 'https://www.microcenter.com/product/684484/asus-b650-plus-tuf-gaming-wifi-atx-am5-motherboard'],
        'ASUS B650-E TUF Gaming WiFi': ['ASUS B650-E TUF Gaming WiFi', '179.99(sale)', 'https://www.microcenter.com/product/684484/asus-b650-e-tuf-gaming-wifi-amd-am5-atx-motherboard'],
        'MSI B550 MAG Tomahawk Max WiFi': ['MSI B550 MAG Tomahawk Max WiFi', '149.99(sale)', 'https://www.microcenter.com/product/684484/msi-b550-mag-tomahawk-max-wifi-amd-am4-atx-motherboard'],
        'ASUS Z790-V Prime AX DDR5': ['ASUS Z790-V Prime AX DDR5', '219.99', 'https://www.microcenter.com/product/684484/asus-z790-v-prime-ax-intel-lga-1700-atx-motherboard'],
        'ASUS Z790 Prime Gaming WIFI7': ['ASUS Z790 Prime Gaming WIFI7', '179.99(sale)', 'https://www.microcenter.com/product/684484/asus-z790-prime-gaming-wifi7-intel-lga-1700-atx'],
        'MSI Z890 Gaming Plus WiFi': ['MSI Z890 Gaming Plus WiFi', '269.99', 'https://www.microcenter.com/product/684484/msi-z890-gaming-plus-wifi-intel-lga-1851-atx-motherboard']}
ram =  {'G.Skill Flare X5 Series 32GB (2 x 16GB) DDR5-6000 CL36': ['G.Skill Flare X5 Series 32GB (2 x 16GB) DDR5-6000 CL36', '99.99(sale)', 'https://www.microcenter.com/product/685301/g-skill-flare-x5-series-32gb-2-x-16gb-ddr5-6000-pc5-48000-cl36-dual-channel-desktop-memory-kit-f5-6000j3636f16gx2-fx5'],
        'G.Skill Flare X5 Series 64GB (2 x 32GB) DDR5-6000 CL30': ['G.Skill Flare X5 Series 64GB (2 x 32GB) DDR5-6000 CL30', '192.99(sale)', 'https://www.microcenter.com/product/685301/g-skill-flare-x5-series-64gb-2-x-32gb-ddr5-6000-pc5-48000-cl30-dual-channel-desktop-memory-kit-f5-6000j3040g32gx2-fx5'],
        'G.Skill Ripjaws S5 32GB (2 x 16GB) DDR5-6000 CL36': ['G.Skill Ripjaws S5 32GB (2 x 16GB) DDR5-6000 CL36', '99.99(sale)', 'https://www.microcenter.com/product/685301/g-skill-ripjaws-s5-32gb-2-x-16gb-ddr5-6000-pc5-48000-cl36-dual-channel-desktop-memory-kit-f5-6000j3636f16gx2-rs5k'],
        'G.Skill Ripjaws S5 64GB (2 x 32GB) DDR5-6000 CL36': ['G.Skill Ripjaws S5 64GB (2 x 32GB) DDR5-6000 CL36', '199.99(sale)', 'https://www.microcenter.com/product/685301/g-skill-ripjaws-s5-64gb-2-x-32gb-ddr5-6000-pc5-48000-cl36-dual-channel-desktop-memory-kit-f5-6000j3636f32gx2-rs5k']}
gpus = {'Sapphire Technology AMD Radeon RX 7900 XTX Pulse': ['Sapphire Technology AMD Radeon RX 7900 XTX Pulse', '899.99(sale)', 'https://www.microcenter.com/product/685301/sapphire-technology-amd-radeon-rx-7900-xtx-pulse-overclocked-triple-fan-24gb-gddr6-pcie-4-0-graphics-card'],
        'Sapphire Technology AMD Radeon RX 7900 XT Pulse': ['Sapphire Technology AMD Radeon RX 7900 XT Pulse', '679.99(sale)', 'https://www.microcenter.com/product/685301/sapphire-technology-amd-radeon-rx-7900-xt-pulse-overclocked-triple-fan-20gb-gddr6-pcie-4-0-graphics-card'],
        'XFX - Speedster MERC310 AMD Radeon RX 7900XT': ['XFX - Speedster MERC310 AMD Radeon RX 7900XT', '704.99(sale)', 'https://www.bestbuy.com/site/xfx-speedster-merc310-amd-radeon-rx-7900xt-20gb-gddr6-pci-express-4-0-gaming-graphics-card-black-rx-79tmercur/6502084.p?skuId=6502084'],
        'Sapphire Technology AMD Radeon RX 7800 XT Pure': ['Sapphire Technology AMD Radeon RX 7800 XT Pure', '499.99', 'https://www.microcenter.com/product/685301/sapphire-technology-amd-radeon-rx-7800-xt-pure-triple-fan-16gb-gddr6-pcie-4-0-graphics-card'],
        'XFX - SPEEDSTER QICK319 AMD Radeon RX 7700XT BLACK': ['XFX - SPEEDSTER QICK319 AMD Radeon RX 7700XT BLACK', '409.99', 'https://www.bestbuy.com/site/xfx-speedster-qick319-amd-radeon-rx-7700xt-black-12gb-gddr6-pci-express-4-0-gaming-graphics-card-black-rx-77tqickbr/6502085.p?skuId=6502085'],
        'XFX AMD Radeon RX 6750 XT': ['XFX AMD Radeon RX 6750 XT', '324.99', 'https://www.microcenter.com/product/685301/xfx-amd-radeon-rx-6750-xt-triple-fan-12gb-gddr6-pcie-4-0-graphics-card'],
        'PNY GeForce RTX 4080 Super 16GB Verto': ['PNY GeForce RTX 4080 Super 16GB Verto', '1129.99', 'https://www.amazon.com/PNY-GeForce-RTX-4080-Super-16GB-Verto/dp/B0B8Q5Q5Q5'],
        'Gigabyte NVIDIA GeForce RTX 4070 Ti Super': ['Gigabyte NVIDIA GeForce RTX 4070 Ti Super', '824.99(sale)', 'https://www.microcenter.com/product/685301/gigabyte-nvidia-geforce-rtx-4070-ti-super-gaming-rgb-overclocked-triple-fan-16gb-gddr6x-pcie-4-0-graphics-card'],
        'MSI NVIDIA GeForce RTX 4070 Super VENTUS 2X': ['MSI NVIDIA GeForce RTX 4070 Super VENTUS 2X', '624.99', 'https://www.microcenter.com/product/685301/msi-nvidia-geforce-rtx-4070-super-ventus-2x-overclocked-dual-fan-12gb-gddr6x-pcie-4-0-graphics-card'],
        'Zotac NVIDIA GeForce RTX 4070 Twin Edge': ['Zotac NVIDIA GeForce RTX 4070 Twin Edge', '499.99', 'https://www.microcenter.com/product/685301/zotac-nvidia-geforce-rtx-4070-twin-edge-overclocked-dual-fan-12gb-gddr6-pcie-4-0-graphics-card']}
ssds = {'Samsung 990 EVO Plus 1TB': ['Samsung 990 EVO Plus 1TB', '84.99(sale)', 'https://www.microcenter.com/product/685301/samsung-990-evo-plus-1tb-samsung-v-nand-tlc-nand-pcie-gen-4-x4-and-pcie-gen-5-x2-nvme-m2-internal-ssd'],
        'Samsung 990 EVO Plus 4TB': ['Samsung 990 EVO Plus 4TB', '249.99(sale)', 'https://www.microcenter.com/product/685301/samsung-990-evo-plus-4tb-samsung-v-nand-tlc-nand-pcie-gen-4-x4-and-pcie-gen-5-x2-nvme-m2-internal-ssd'],
        'Samsung 990 EVO 1TB': ['Samsung 990 EVO 1TB', '74.99(sale)', 'https://www.microcenter.com/product/685301/samsung-990-evo-1tb-samsung-v-nand-tlc-nand-pcie-gen-4-x4-and-pcie-gen-5-x2-nvme-m2-internal-ssd'],
        'Samsung 990 EVO 2TB': ['Samsung 990 EVO 2TB', '129.99(sale)', 'https://www.microcenter.com/product/685301/samsung-990-evo-2tb-samsung-v-nand-tlc-nand-pcie-gen-4-x4-and-pcie-gen-5-x2-nvme-m2-internal-ssd']}
psus = {'Corsair RM850x': ['Corsair RM850x', '124.99(sale)', 'https://www.microcenter.com/product/685301/corsair-rm850x-850-watt-cybenetics-gold-atx-fully-modular-power-supply'],
        'Corsair RM1000x': ['Corsair RM1000x', '164.99(sale)', 'https://www.microcenter.com/product/685301/corsair-rm1000x-1000-watt-cybenetics-gold-atx-fully-modular-power-supply'],
        'Corsair RMx SHIFT Series RM850x': ['Corsair RMx SHIFT Series RM850x', '124.99(sale)', 'https://www.microcenter.com/product/685301/corsair-rmx-shift-series-rm850x-850-watt-80-plus-gold-fully-modular-atx-power-supply'],
        'Corsair RMx SHIFT Series RM1000x': ['Corsair RMx SHIFT Series RM1000x', '164.99(sale)', 'https://www.microcenter.com/product/685301/corsair-rmx-shift-series-rm1000x-1000-watt-80-plus-gold-fully-modular-atx-power-supply']}
cases = {'Fractal Design Torrent RGB Tempered Glass': ['Fractal Design Torrent RGB Tempered Glass', '229.99', 'https://www.microcenter.com/product/685301/fractal-design-torrent-rgb-tempered-glass-atx-mid-tower-computer-case'],
        'Fractal Design Pop XL Air RGB Tempered Glass': ['Fractal Design Pop XL Air RGB Tempered Glass', '114.99', 'https://www.microcenter.com/product/685301/fractal-design-pop-xl-air-rgb-tempered-glass-atx-mid-tower-computer-case'],
        'Fractal Design North Tempered Glass': ['Fractal Design North Tempered Glass', '149.99', 'https://www.microcenter.com/product/685301/fractal-design-north-tempered-glass-atx-mid-tower-computer-case'],
        'Fractal Design North Mesh': ['Fractal Design North Mesh', '149.99', 'https://www.microcenter.com/product/685301/fractal-design-north-mesh-atx-mid-tower-computer-case'],
        'Lian Li O11D EVO RGB Tempered Glass': ['Lian Li O11D EVO RGB Tempered Glass', '159.99', 'https://www.microcenter.com/product/685301/lian-li-o11d-evo-rgb-tempered-glass-atx-mid-tower-computer-case'],
        'Corsair 5000D Airflow Tempered Glass': ['Corsair 5000D Airflow Tempered Glass', '174.99', 'https://www.microcenter.com/product/685301/corsair-5000d-airflow-tempered-glass-mid-tower-atx-computer-case'],
        'Corsair 7000D AIRFLOW Tempered Glass': ['Corsair 7000D AIRFLOW Tempered Glass', '209.99', 'https://www.microcenter.com/product/685301/corsair-7000d-airflow-tempered-glass-eatx-full-tower-computer-case']}
app = dash.Dash()
app.layout = html.Div(
        style={'text-align':'center'},
        children=[
                html.H1(
                        children='PC Part Picker but Worse',
                        style={'color':'black'}
                ),
                dcc.Dropdown(
                        id = 'cpu dropdown',
                        options=[{'label':'7800x3d', 'value':'7800x3d'},
                                 {'label':'9800x3d', 'value':'9800x3d'},
                                 {'label':'5700x3d', 'value':'5700x3d'},
                                 {'label':'7600x3d', 'value':'7600x3d'},
                                 {'label':'i7-14700k', 'value':'i7-14700k'},
                                 {'label':'Ultra 7 265K', 'value':'Ultra 7 265K'},
                                 {'label':'i9-12900k', 'value':'i9-12900k'},],
                        style={'width':'50%', 'margin':'auto'}
                ),
                dcc.Dropdown(
                        id = 'mb dropdown',
                        options=[{'label': 'ASRock X870 Pro RS WiFi', 'value': 'ASRock X870 Pro RS WiFi'},
                                 {'label': 'ASUS B650-PLUS TUF GAMING WIFI', 'value': 'ASUS B650-PLUS TUF GAMING WIFI'},
                                 {'label': 'ASUS B650-E TUF Gaming WiFi', 'value': 'ASUS B650-E TUF Gaming WiFi'},
                                 {'label': 'MSI B550 MAG Tomahawk Max WiFi', 'value': 'MSI B550 MAG Tomahawk Max WiFi'},
                                 {'label': 'ASUS Z790-V Prime AX DDR5', 'value': 'ASUS Z790-V Prime AX DDR5'},
                                 {'label': 'ASUS Z790 Prime Gaming WIFI7', 'value': 'ASUS Z790 Prime Gaming WIFI7'},
                                 {'label': 'MSI Z890 Gaming Plus WiFi', 'value': 'MSI Z890 Gaming Plus WiFi'}],
                        style={'width':'50%', 'margin':'auto'}
                ),
                dcc.Dropdown(
                        id = 'gpu dropdown',
                        options=[{'label': 'Sapphire Technology AMD Radeon RX 7900 XTX Pulse', 'value': 'Sapphire Technology AMD Radeon RX 7900 XTX Pulse'},
                                 {'label': 'Sapphire Technology AMD Radeon RX 7900 XT Pulse', 'value': 'Sapphire Technology AMD Radeon RX 7900 XT Pulse'},
                                 {'label': 'XFX - Speedster MERC310 AMD Radeon RX 7900XT', 'value': 'XFX - Speedster MERC310 AMD Radeon RX 7900XT'},
                                 {'label': 'Sapphire Technology AMD Radeon RX 7800 XT Pure', 'value': 'Sapphire Technology AMD Radeon RX 7800 XT Pure'},
                                 {'label': 'XFX - SPEEDSTER QICK319 AMD Radeon RX 7700XT BLACK', 'value': 'XFX - SPEEDSTER QICK319 AMD Radeon RX 7700XT BLACK'},
                                 {'label': 'XFX AMD Radeon RX 6750 XT', 'value': 'XFX AMD Radeon RX 6750 XT'},
                                 {'label': 'PNY GeForce RTX 4080 Super 16GB Verto', 'value': 'PNY GeForce RTX 4080 Super 16GB Verto'},
                                 {'label': 'Gigabyte NVIDIA GeForce RTX 4070 Ti Super', 'value': 'Gigabyte NVIDIA GeForce RTX 4070 Ti Super'},
                                 {'label': 'MSI NVIDIA GeForce RTX 4070 Super VENTUS 2X', 'value': 'MSI NVIDIA GeForce RTX 4070 Super VENTUS 2X'},
                                 {'label': 'Zotac NVIDIA GeForce RTX 4070 Twin Edge', 'value': 'Zotac NVIDIA GeForce RTX 4070 Twin Edge'}],
                        style={'width':'50%', 'margin':'auto'}
                ),
                dcc.Dropdown(
                        id = 'ram dropdown',
                        options=[{'label': 'G.Skill Flare X5 Series 32GB (2 x 16GB) DDR5-6000 CL36', 'value': 'G.Skill Flare X5 Series 32GB (2 x 16GB) DDR5-6000 CL36'},
                                 {'label': 'G.Skill Flare X5 Series 64GB (2 x 32GB) DDR5-6000 CL30', 'value': 'G.Skill Flare X5 Series 64GB (2 x 32GB) DDR5-6000 CL30'},
                                 {'label': 'G.Skill Ripjaws S5 32GB (2 x 16GB) DDR5-6000 CL36', 'value': 'G.Skill Ripjaws S5 32GB (2 x 16GB) DDR5-6000 CL36'},
                                 {'label': 'G.Skill Ripjaws S5 64GB (2 x 32GB) DDR5-6000 CL36', 'value': 'G.Skill Ripjaws S5 64GB (2 x 32GB) DDR5-6000 CL36'}],
                        style={'width':'50%', 'margin':'auto'}
                ),
                dcc.Dropdown(
                        id='ssd dropdown',
                        options= [{'label': 'Samsung 990 EVO Plus 1TB', 'value': 'Samsung 990 EVO Plus 1TB'},
                                  {'label': 'Samsung 990 EVO Plus 4TB', 'value': 'Samsung 990 EVO Plus 4TB'},
                                  {'label': 'Samsung 990 EVO 1TB', 'value': 'Samsung 990 EVO 1TB'},
                                  {'label': 'Samsung 990 EVO 2TB', 'value': 'Samsung 990 EVO 2TB'}],
                        style={'width': '50%', 'margin': 'auto'}
                ),
                dcc.Dropdown(
                        id='psu dropdown',
                        options=[{'label': 'Corsair RM850x', 'value': 'Corsair RM850x'},
                                 {'label': 'Corsair RM1000x', 'value': 'Corsair RM1000x'},
                                 {'label': 'Corsair RMx SHIFT Series RM850x', 'value': 'Corsair RMx SHIFT Series RM850x'},
                                 {'label': 'Corsair RMx SHIFT Series RM1000x', 'value': 'Corsair RMx SHIFT Series RM1000x'}],
                        style={'width': '50%', 'margin': 'auto'}
                ),
                dcc.Dropdown(
                        id='case dropdown',
                        options=[{'label': 'Fractal Design Torrent RGB Tempered Glass', 'value': 'Fractal Design Torrent RGB Tempered Glass'},
                                 {'label': 'Fractal Design Pop XL Air RGB Tempered Glass', 'value': 'Fractal Design Pop XL Air RGB Tempered Glass'},
                                 {'label': 'Fractal Design North Tempered Glass', 'value': 'Fractal Design North Tempered Glass'},
                                 {'label': 'Fractal Design North Mesh', 'value': 'Fractal Design North Mesh'},
                                 {'label': 'Lian Li O11D EVO RGB Tempered Glass', 'value': 'Lian Li O11D EVO RGB Tempered Glass'},
                                 {'label': 'Corsair 5000D Airflow Tempered Glass', 'value': 'Corsair 5000D Airflow Tempered Glass'},
                                 {'label': 'Corsair 7000D AIRFLOW Tempered Glass', 'value': 'Corsair 7000D AIRFLOW Tempered Glass'}],
                        style={'width': '50%', 'margin': 'auto'}
                ),
                html.Div(id='selected-parts', style={'color': 'black', 'margin-top': '20px'}),
                html.Div(id='total-price', style={'color': 'black', 'margin-top': '20px'})
    ]
)
@app.callback(
    [Output('selected-parts', 'children'),
     Output('total-price', 'children')],
    [Input('cpu dropdown', 'value'),
     Input('mb dropdown', 'value'),
     Input('gpu dropdown', 'value'),
     Input('ram dropdown', 'value'),
     Input('ssd dropdown', 'value'),
     Input('psu dropdown', 'value'),
     Input('case dropdown', 'value')]
)
def update_parts(cpu, mb, gpu, RAM, ssd, psu, case):
    parts = {'CPU': cpu, 'Motherboard': mb, 'GPU': gpu, 'RAM': RAM, 'SSD': ssd, 'PSU': psu, 'Case': case}
    part_details = []
    total_price = 0.0

    for part_type, part in parts.items():
        if part:
            if part_type == 'CPU':
                details = cpus[part]
            elif part_type == 'Motherboard':
                details = mbs[part]
            elif part_type == 'GPU':
                details = gpus[part]
            elif part_type == 'RAM':
                details = ram[part]
            elif part_type == 'SSD':
                details = ssds[part]
            elif part_type == 'PSU':
                details = psus[part]
            elif part_type == 'Case':
                details = cases[part]

            part_details.append(html.Div([
                html.H4(f"{part_type}: {details[0]}"),
                html.P(f"Price: ${details[1]}"),
                html.A("Link", href=details[2], target="_blank")
            ]))
            price = float(details[1].replace('(sale)', '').replace('$', ''))
            total_price += price

    total_price_div = html.H3(f"Total Price: ${total_price:.2f}")

    return part_details, total_price_div
if __name__ == '__main__':
        app.run_server(debug=False)