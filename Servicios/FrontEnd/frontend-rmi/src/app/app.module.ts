import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { InvestigadorComponent } from './components/home/investigador/investigador.component';
import { AdministradorComponent } from './components/home/administrador/administrador.component';
import { CrearInvestigadorComponent } from './components/home/administrador/crear-investigador/crear-investigador.component';
import { GestionarInvestigadorComponent } from './components/home/administrador/gestionar-investigador/gestionar-investigador.component';

import { BrowserAnimationsModule} from '@angular/platform-browser/animations';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    InvestigadorComponent,
    AdministradorComponent,
    CrearInvestigadorComponent,
    GestionarInvestigadorComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatProgressSpinnerModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
