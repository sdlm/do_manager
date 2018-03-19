#/usr/bin/python3.6

import digitalocean

TOKEN = 'You_DigitalOcean_token'


if __name__ == '__main__':
    droplets = []
    for i in range(5):
        droplet = digitalocean.Droplet(token=TOKEN,
                                       name=f'sandbox-{i}',
                                       region='fra1',
                                       image='ubuntu-17-10-x64',
                                       size_slug='1gb')
        droplet.create()
        droplets.append(droplet)
    print(f'create {len(droplets)} droplets !')

    for d in droplets:
        d.destroy()
    print(f'destroy {len(droplets)} droplets !')
