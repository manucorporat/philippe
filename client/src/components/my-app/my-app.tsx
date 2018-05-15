import '@ionic/core';
import { Component, Prop } from '@stencil/core';

@Component({
  tag: 'my-app',
  styleUrl: 'my-app.scss'
})
export class MyApp {

  @Prop({connect: 'ion-loading-controller'}) loadingCtrl: HTMLIonLoadingControllerElement;

  async componentDidLoad() {
    const loading = await this.loadingCtrl.create({
      content: 'buscando a philippe...'
    });
    await loading.present();
    await searchPhilippe();
    await loading.dismiss();
  }

  render() {
    return (
      <ion-app>
        <ion-router useHash={false}>
          <ion-route url='/' component='home-page'></ion-route>
          <ion-route url='/settings' component='settings-page'></ion-route>
        </ion-router>
        <ion-nav></ion-nav>
      </ion-app>
    );
  }
}

async function searchPhilippe() {
  await wait(3000);
}

async function wait(time: number) {
  return new Promise((resolve) => {
    setTimeout(resolve, time);
  });
}
