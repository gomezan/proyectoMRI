import { TestBed } from '@angular/core/testing';

import { ModeloUsuarioService } from './modelo-usuario.service';

describe('ModeloUsuarioService', () => {
  let service: ModeloUsuarioService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ModeloUsuarioService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
