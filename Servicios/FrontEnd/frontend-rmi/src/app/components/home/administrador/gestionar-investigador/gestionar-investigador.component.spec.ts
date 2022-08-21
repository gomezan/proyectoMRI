import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GestionarInvestigadorComponent } from './gestionar-investigador.component';

describe('GestionarInvestigadorComponent', () => {
  let component: GestionarInvestigadorComponent;
  let fixture: ComponentFixture<GestionarInvestigadorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GestionarInvestigadorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GestionarInvestigadorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
