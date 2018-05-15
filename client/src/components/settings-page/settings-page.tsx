import { Component } from '@stencil/core';


@Component({
  tag: 'settings-page',
  styleUrl: 'settings-page.scss'
})
export class SettingsPage {

  private settings = [
    {
      name: 'PID (proporcional)',
      min: -100,
      max: 100,
      value: 20,
    },
    {
      name: 'PID (integral)',
      min: -10,
      max: 10,
      value: 0,
    },
    {
      name: 'PID (derivativa)',
      min: 0,
      max: 100,
      value: 20,
    },
    {
      name: 'Velocidad máxima',
      min: 0,
      max: 10,
      value: 5,
    }
  ]

  render() {
    return [
      <ion-header>
        <ion-toolbar color='primary'>
          <ion-buttons slot="start">
            <ion-back-button defaultHref="/"/>
          </ion-buttons>
          <ion-title>Ajustes</ion-title>
        </ion-toolbar>
      </ion-header>,

      <ion-content>
        {this.settings.map(s => (
          <ion-list>
            <ion-list-header>{s.name}</ion-list-header>
            <ion-item>
              <ion-range min={s.min} max={s.max} value={s.value} pin={true}>
                <div slot="start" class="range-data">{s.min}</div>
                <div slot="end" class="range-data">{s.max}</div>
              </ion-range>
            </ion-item>
          </ion-list>
        ))}
      </ion-content>
    ];
  }
}
