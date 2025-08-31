import { expect, test } from 'vitest';
import { response_verifier, server } from './setup';
import { SendResult } from '/cas/LmatCasServer';
import { TestHangArgsPayload, TestHangMessage } from '/cas/messages/test_messages/TestHangMessage';
import { HandlerInterrupter } from '/HandlerInterrupter';

test('Test CAS Initialize and Shutdown', () => { 
    // everything is handled in the before and after things so no need to do anything here...
});

test('Test CAS Handler Interruption', async () => {

    const sent_messages: SendResult[] = [ ];

    const message_count = 100;

    for(let i = 0; i < message_count; i++) {
        sent_messages.push(server.send(new TestHangMessage(new TestHangArgsPayload(60))));
    }

    expect(server.getCurrentMessages().length).toBe(message_count);
    
    const handler_interrupter = new HandlerInterrupter(server, response_verifier);
    
    await new Promise<void>((resolve) => setTimeout(resolve, 5000));
    
    handler_interrupter.interruptAllHandlers();

    await Promise.all(sent_messages.map(x => expect(x.response).rejects.toThrow('Interrupted')));
});
