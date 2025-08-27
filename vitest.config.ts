import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    root: './src',
    setupFiles: [ 'tests/setup.ts' ],
    testTimeout: 60000
  }
});