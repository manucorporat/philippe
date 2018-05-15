import { Component } from '@stencil/core';

@Component({
  tag: 'home-page',
  styleUrl: 'home-page.scss'
})
export class HomePage {

  private chartEl: HTMLElement;

  componentDidLoad() {
    // this.chartEl.
  }

  render() {
    return [
      <ion-header>
        <ion-toolbar color='primary'>
          <ion-title>Philippe</ion-title>
          <ion-buttons slot="primary">
            <ion-button href="/settings">
              <ion-icon name="settings" slot="icon-only"/>
            </ion-button>
          </ion-buttons>
        </ion-toolbar>
      </ion-header>,

      <ion-content padding scrollEnabled={false}>
        <div ref={(el) => this.chartEl = el}class="chart"></div>

        <div class="controller">
          <ion-button expand="block" size="large" class="left">
            <ion-icon name="arrow-back"/>
          </ion-button>

          <ion-button expand="block" size="large" class="right">
            <ion-icon name="arrow-forward"/>
          </ion-button>

          <ion-button expand="block" size="large" class="up">
            <ion-icon name="arrow-up"/>
          </ion-button>

          <ion-button expand="block" size="large" class="down">
            <ion-icon name="arrow-down"/>
          </ion-button>
        </div>

      </ion-content>
    ];
  }
}
