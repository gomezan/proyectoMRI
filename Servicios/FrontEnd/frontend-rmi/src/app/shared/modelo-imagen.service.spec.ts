import { TestBed } from '@angular/core/testing';

import { ModeloImagenService } from './modelo-imagen.service';

describe('ModeloImagenService', () => {
  let service: ModeloImagenService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ModeloImagenService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
