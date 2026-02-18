
'use client';

import React from 'react';
import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';
import Link from 'next/link';
import './Footer.css';

const Footer = () => {
    return (
        <footer className="footer-container">
            <div className="footer-inner">
                {/* Column 1: Quick Links */}
                <div className="footer-column">
                    <h3>Quick Links</h3>
                    <ul>
                        <li><Link href="/about">About Us</Link></li>
                        <li><Link href="/contact">Contact</Link></li>
                        <li><Link href="/faq">FAQ</Link></li>
                    </ul>
                </div>

                {/* Column 2: Contact Info */}
                <div className="footer-column">
                    <h3>Contact</h3>
                    <p>1234 Food St, Dallas, TX 12345</p>
                    <p>Phone: (123) 456-7890</p>
                    <p>Email: hello@foodmarketplace.com</p>
                </div>

                {/* Column 3: Social Media */}
                <div className="footer-column">
                    <h3>Follow Us</h3>
                    <div className="social-icons">
                        <a href="https://facebook.com" target="_blank"><FaFacebook /></a>
                        <a href="https://twitter.com" target="_blank"><FaTwitter /></a>
                        <a href="https://instagram.com" target="_blank"><FaInstagram /></a>
                    </div>
                </div>

                {/* Column 4: Newsletter */}
                <div className="footer-column">
                    <h3>Newsletter</h3>
                    <p>Stay updated with trending dishes and local gems.</p>
                    <form className="newsletter-form">
                        <input type="email" placeholder="Your email" />
                        <button type="submit">Subscribe</button>
                    </form>
                </div>
            </div>

            <div className="footer-bottom">
                <p>&copy; {new Date().getFullYear()} Indian Food Marketplace - Dallas. All rights reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;

