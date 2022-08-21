import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { InvestigadorComponent } from './components/home/investigador/investigador.component';
import { AdministradorComponent } from './components/home/administrador/administrador.component';
import { CrearInvestigadorComponent } from './components/home/administrador/crear-investigador/crear-investigador.component';
import { GestionarInvestigadorComponent } from './components/home/administrador/gestionar-investigador/gestionar-investigador.component';
import { AuthGuard } from './guards/auth.guard';

const routes: Routes = [
  {path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'home/:iid/investigador', component: InvestigadorComponent,  canActivate: [AuthGuard] },
  { path: 'home/:aid/administrador', component: AdministradorComponent,  canActivate: [AuthGuard] },
  { 
    path: 'home/:aid/administrador/crear-investigador', 
    component: CrearInvestigadorComponent,
    canActivate: [AuthGuard]
  },
  { 
    path: 'home/:aid/administrador/gestionar-investigador/:iid', 
    component: GestionarInvestigadorComponent,
    canActivate: [AuthGuard] 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [AuthGuard]
})
export class AppRoutingModule { }
