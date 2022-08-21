import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearInvestigadorComponent } from './crear-investigador.component';

describe('CrearInvestigadorComponent', () => {
  let component: CrearInvestigadorComponent;
  let fixture: ComponentFixture<CrearInvestigadorComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CrearInvestigadorComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CrearInvestigadorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
